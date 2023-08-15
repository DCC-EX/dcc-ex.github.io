.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst
|EX-BP-LOGO|

********************************************************************************************
Example - Full automation with pin based turnouts and signals on MCP23017 I/O expander Vpins
********************************************************************************************

|tinkerer| |engineer|

.. code-block:: 

  // myAutomation.h for SEQUENCEs with pin based turnouts, sensors, and signals via MCP23017 I/O expander Vpins.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 166)
  ALIAS(SNS2_MAIN_TRN1_EX, 167)
  ALIAS(SNS3_STN, 168)
  ALIAS(SNS4_MAIN_TRN2_APP, 169)
  ALIAS(SNS5_STN_TRN2_APP, 170)
  ALIAS(SNS6_TRN2_EX, 171)
  ALIAS(SIG1_TRN1_APP, 172)
  ALIAS(SIG2_TRN2_GO, 175)
  ALIAS(SIG3_STN_EX, 178)
  ALIAS(BLK1_TRN1_APP, 1)
  ALIAS(BLK2_MAIN_HOLD, 2)
  ALIAS(BLK3_STN, 3)
  ALIAS(BLK4_TRN2_EX, 4)
  ALIAS(BLK1_EXIT, 1)
  ALIAS(BLK1_BLK2, 2)
  ALIAS(BLK1_BLK3, 3)
  ALIAS(BLK2_BLK4, 4)
  ALIAS(BLK3_BLK4, 5)
  ALIAS(BLK4_BLK1, 6)
  ALIAS(CHOOSE_BLK2, 60)

  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 173, 174)
  SIGNAL(SIG2_TRN2_GO, 176, 177)
  SIGNAL(SIG3_STN_EX, 179, 180)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // Send three locos around our layout:
  RESERVE(BLK1_TRN1_APP)
  RESERVE(BLK2_MAIN_HOLD)
  RESERVE(BLK4_TRN2_EX)
  SENDLOCO(1, BLK1_EXIT)
  SENDLOCO(2, BLK2_BLK4)
  SENDLOCO(3, BLK4_BLK1)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Sequence to exit block 1, and choose whether to go to the station or continue on main
  SEQUENCE(BLK1_EXIT)
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

  // Sequence to go from block 1 to block 2
  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      CLOSE(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

  // Sequence to go from block 1 to block 3
  SEQUENCE(BLK1_BLK3)
    RESERVE(BLK3_STN)
    IFCLOSED(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      THROW(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(10)
    AT(SNS3_STN)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

  // Sequence to go from block 2 to block 4
  SEQUENCE(BLK2_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFTHROWN(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      CLOSE(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG2_TRN2_GO)
    FWD(20)
    AFTER(SNS4_MAIN_TRN2_APP)
    FREE(BLK2_MAIN_HOLD)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to go from block 3 to block 4
  SEQUENCE(BLK3_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFCLOSED(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      THROW(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG3_STN_EX)
    FWD(20)
    AFTER(SNS5_STN_TRN2_APP)
    FREE(BLK3_STN)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to move from block 4 back to block 1
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(30)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)
