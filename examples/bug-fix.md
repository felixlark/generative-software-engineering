# Example: user-visible bug fix

## Intent

A user reports that saving settings appears successful but the change is lost after restart.

## Outcome contract

The saved value must survive restart. Existing unrelated settings must remain unchanged. Completion requires evidence for persistence logic and the actual restart path.

## Organization decision

The root GSE keeps implementation and verification because the change is localized and sequential. A sub-agent would add handoff cost without independent work or specialist value.

## Work

The root GSE inspects the current persistence path, reproduces the failure, identifies the missing write, implements the smallest correction, and avoids adding a new storage abstraction because the existing store already owns persistence.

## Evidence

A focused persistence test proves the corrected serialization behavior. The exact runnable candidate is then used to change the setting, restart the program, and observe the retained value. The user-path evidence is collected after the final code change.

## Completion

The outcome closes when both the persistence claim and restart behavior are evidenced and no relevant regression remains. Passing only the focused test would be an incomplete result because it cannot prove the restart wiring.
