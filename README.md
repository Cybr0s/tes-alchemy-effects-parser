### 🧪 **The Elder Scrolls Alchemy Effects Parser**
A custom data-cleaning script created to process and unify alchemy reagent data scraped from the [Unofficial Elder Scrolls Pages](https://en.uesp.net/wiki/Lore:Alchemy_A), as part of a personal role-playing experience in The Elder Scrolls universe.

### 📌 **Purpose**
This script parses a messy export of alchemy effects across different TES games — such as The Elder Scrolls Online, Oblivion, Skyrim, etc. — and:

- Removes duplicate effect entries

- Normalizes inconsistent naming (e.g. Heal Health vs. Restore Health)

- Outputs a cleaner, unified list of effects per reagent

#### Example transformation:

##### Input (raw):
```text
Aloe Vera Leaves
    Heal Health
    Heal Health
    Restore Health
    Restore Health
    Restore Fatigue
    Restore Health
    Damage Magicka
    Invisibility
    Restore Health
    Restore Stamina
    Damage Magicka
    Invisibility
```
##### Output (cleaned):
```text
Aloe Vera Leaves
    Health Restoration
    Fatigue Restoration
    Magicka Damage
    Invisibility
    Stamina Restoration
```
## 🎯 Motivation
Originally built for a richer and easier role-play experience for me and my friend, whose characters are alchemists. Together, we designed the naming convention for the alchemy related magical effects across all the games in the series. After that, I wrote the script to implement that.

The .txt file with the end result is added, so if you are, too, a member of TES role-play community and have interest in alchemy, feel free to use it!


## ⚠️ Disclaimer
This was a one-time-use script built specifically for the structure of the UESP alchemy wiki page.
It is not a general-purpose parser and may not work on other datasets without modification. Shared here not as a reusable tool but as part of my learning journey. Thank you for your interest.
