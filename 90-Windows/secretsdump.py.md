# secretsdump
-user-status
-pwd-last-set
-history

```bash
secretsdump.py -pwd-last-set -user-status -history -ntds ntds.dit -security SECURITY -system SYSTEM local | tee secretsdump.bacup
```

