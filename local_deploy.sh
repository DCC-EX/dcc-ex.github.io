#!/bin/bash

## hint for haba:
##/usr/bin/kinit -t /etc/krb5.keytab host/bento.stacken.kth.se bash -c 'chown haba `echo $KRB5CCNAME  | sed s/FILE://1` ; su haba bash -c "afslog -c stacken.kth.se; tokens; touch foo; kdestroy"'

# runs only on haba's deploy:
type -p afslog > /dev/null && afslog
type -p klist > /dev/null && klist
test -f `echo $KRB5CCNAME  | sed s/FILE://1` && ls -l `echo $KRB5CCNAME  | sed s/FILE://1`

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
set -x
while sleep 60 && touch ../run/timestamp; do

    git fetch --dry-run 2>&1 | cut -c 26- | awk ' $2 == "->" && $1 != "gh-pages" { print "touch ../branch/"$1"/update-me"}' | bash

    for DIR in `ls -d ../branch/*/update-me 2>/dev/null`  ; do
	BRANCH=`echo $DIR | awk -F/ '{print $3}'`
	#BRANCH=`git branch | egrep '^\*' | sed 's/. //1'`
	git checkout "$BRANCH"                                           2>&1 | cat > "../branch/$BRANCH/lastrun.log"
	git pull                                                         2>&1 | cat >> "../branch/$BRANCH/lastrun.log"
	pip3 install -r requirements.txt                                 2>&1 | cat >> "../branch/$BRANCH/lastrun.log"
	sphinx-build -M html docs/. "../branch/$BRANCH/" -W --keep-going --write-all --fresh-env 2>&1 | cat >> "../branch/$BRANCH/lastrun.log"
	rm "../branch/$BRANCH/update-me"
    done
    # still in testing, break here
    # break
done

#deactivate venv
deactivate

exit 0
