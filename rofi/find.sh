if [ ! -z "$@" ]
then
  QUERY=$@
  if [[ "$@" == /* ]]
  then
    if [[ "$@" == *\?\? ]]
    then
      coproc ( exo-open "${QUERY%\/* \?\?}"  > /dev/null 2>&1 )
      exec 1>&-
      exit;
    else
      coproc ( exo-open "$@"  > /dev/null 2>&1 )
      exec 1>&-
      exit;
    fi
  elif [[ "$@" == \!\!* ]]
  then
    echo "search files"
  elif [[ "$@" == \?* ]]
  then
    while read -r line; do
      echo "$line" \?\?
    done <<< $(find / -iname *"${QUERY#\?}"* 2>&1 | grep -v 'Permission denied\|Input/output error')
  else
    find / -iname *"${QUERY#!}"* 2>&1 | grep -v 'Permission denied\|Input/output error'
  fi
else
  echo "search files"
fi
