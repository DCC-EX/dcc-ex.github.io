#!/bin/bash

## hint for haba:
##/usr/bin/kinit -t /etc/krb5.keytab host/bento.stacken.kth.se bash -c 'chown haba `echo $KRB5CCNAME  | sed s/FILE://1` ; su haba bash -c "afslog -c stacken.kth.se; tokens; touch foo; kdestroy"'

# runs only on haba's deploy:
type -p afslog > /dev/null && afslog

# here is the real start
##########################

# check if we already have a venv prepared (if yes, we use that)
if test -d venv ; then
    : all well
else
    python3 -m venv venv || exit 255
fi

# activate prepared venv
. venv/bin/activate

while sleep 1; do

    git fetch --dry-run 2>&1 | awk ' $4 != "" { print "touch ../branch/"$2"/update-me"}' | bash

    for DIR in ../branch/*/update-me ; do
	BRANCH=`echo $DIR | awk -F/ '{print $3}'`
	#BRANCH=`git branch | egrep '^\*' | sed 's/. //1'`
	git checkout "$BRANCH"
	git pull
	pip3 install -r requirements.txt || exit 255
	sphinx-build -M html docs/. "../branch/$BRANCH/" -W --keep-going 2>&1 | cat > "../branch/$BRANCH/lastrun.log"
	rm "../branch/$BRANCH/update-me"
    done
    # still in testing, break here
    break
done

#deactivate venv
deactivate

exit 0
