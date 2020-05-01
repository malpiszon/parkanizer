# Parkanizer API checker
Check if there are free parking spots in OBC F parking

## To send email with results
```bash
content=`./parkanizer.py` && [ "${content}" != "" ] && echo "${content}" | mail -s "Wolne miejsca OBC" recipient1@address.pl,recipient2@address.pl
```
