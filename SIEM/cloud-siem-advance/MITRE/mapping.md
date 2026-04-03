# MITRE ATT&CK Mapping

## SSH Brute Force Detection
- Technique: T1110 (Brute Force)
- Description: Detect repeated failed SSH login attempts
- Detection: Log-based detection from /var/log/auth.log

## File Integrity Monitoring (FIM)
- Technique: T1565.001 (Data Manipulation)
- Description: Detect unauthorized file changes
- Detection: Hash comparison

## Malware Hash Detection
- Technique: T1204 (User Execution)
- Description: Detect known malicious files using hashes

## Persistence (Future Scope)
- Technique: T1547 (Boot or Logon Autostart)
