# Marmot Android deploy (minimal)

Build on **marmot**, install the APK on your **phone** from your laptop. No CLI/server deploy on marmot.

## One-time on marmot

1. Clone this repo (once git remote exists), e.g. `~/Dev/verb-notecard-app`.
2. Install **JDK 17** and **Android SDK** (cmdline tools + platform 34 + build-tools). Set in `~/.profile` or `~/.bashrc`:

   ```bash
   export ANDROID_HOME="$HOME/Android/Sdk"
   export PATH="$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools"
   ```

3. Optional `~/.ssh/config` on your laptop:

   ```
   Host marmot
     HostName marmot
     User thelemur
     IdentityFile ~/.ssh/thelemur-marmot-id_rsa
   ```

## Trigger full remote build

```bash
ssh marmot 'bash -lc "$HOME/Dev/verb-notecard-app/scripts/deploy/marmot/remote/deploy.sh"'
```

Override repo path:

```bash
ssh marmot 'REPO_ROOT=$HOME/Dev/verb-notecard-app bash -lc "$REPO_ROOT/scripts/deploy/marmot/remote/deploy.sh"'
```

Script prints a line `ARTIFACT=/path/to/app-debug.apk` for tooling.

## Pull APK and install on phone (laptop)

USB debugging on, `adb devices` shows phone, then from **this repo on your laptop**:

```bash
./scripts/deploy/marmot/pull-and-install.sh
```

Or manual:

```bash
APK=$(ssh marmot 'bash -lc "$HOME/Dev/verb-notecard-app/scripts/deploy/marmot/remote/deploy.sh"' | tee /dev/stderr | sed -n 's/^ARTIFACT=//p')
scp marmot:"$APK" /tmp/verbpractice-debug.apk
adb install -r /tmp/verbpractice-debug.apk
```

## Remote script only (no install)

| Step | Command |
|------|---------|
| Pull + build | `ssh marmot '…/remote/deploy.sh'` |
| Pull only | `ssh marmot '…/remote/deploy.sh --pull'` |
| Build only (no git) | `ssh marmot '…/remote/deploy.sh --build'` |
