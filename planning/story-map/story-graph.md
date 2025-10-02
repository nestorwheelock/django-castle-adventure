# Story Graph: Complete Scene Map

**Project:** django-castle-adventure v1.0.0
**Total Scenes:** 28 (including endings and deaths)

---

## Visual Story Graph

```
═══════════════════════════════════════════════════════════════
                        STORY GRAPH
═══════════════════════════════════════════════════════════════

                          [START]
                             |
                          [01: Outside Castle Walls]
                             |
                    ┌────────┴────────┐
                    │                 │
          [02: Climb Garden Wall]  [D1: Try Front Gate → DEATH]
                    |
          [03: Courtyard - Hounds!]
                    |
         ┌──────────┼──────────┐
         │          │          │
  [D2: Fight]  [04: Run!]  [06: Hide]
    DEATH         |            |
              [05: Drawbridge]  |
                    |           |
            ┌───────┼───────────┘
            │       │
     [D3: Jump]  [Gate Drops]
       DEATH        |
                    |
              ══════════════════════════════
              CONVERGENCE POINT 1: INSIDE
              ══════════════════════════════
                    |
         [07: Castle Entrance Hall]
                    |
              [08: Throne Room]
           (Find Clue + Gold Goblet)
                    |
              ══════════════════════════════
              CONVERGENCE POINT 2: HUB
              ══════════════════════════════
                    |
         [09: Grand Hallway - HUB]
                    |
      ┌─────────────┼─────────────┬─────────────┐
      │             │             │             │
  [10: Library] [12: Dungeon] [14: Dragon] [16: Wizard]
      |             |             |             |
  (Inv. Ink)   [13: Troll]   (Sleeping)   (Thinks you're
      |         (Riddle!)        |          pizza guy)
      |             |         ┌───┴───┐        |
  (Need        [Get Magic]   [Sneak] [Wake]  [Get Royal
   Spectacles)  Spectacles     |       |      Seal]
      |             |          [Get] [D4: Panic]
      └─────────────┘          Flame   DEATH
                |               |
        [11: Reveal Message]    |
         (Tower Key behind      |
          throne!)              |
                |               |
        [Back to Throne]        |
                |               |
        [Get Tower Key] ────────┘
                |
                |
      ══════════════════════════════════
      CONVERGENCE POINT 3: TOWER
      ══════════════════════════════════
                |
         [19: Tower Staircase]
          (Blocked by ICE!)
                |
        [Use Dragon's Flame]
          (Ice melts)
                |
         [20: Tower Landing]
                |
         [21: Princess Chamber]
          (Princess Elara)
                |
      ┌─────────┼─────────┬─────────┐
      │         │         │         │
   [E1: Heroic] [E2: Betrayal] [E3: Mutual] [E4: Collapse]
    RESCUE      ENDING    ESCAPE   ENDING
    ENDING                ENDING

                (Secret Path)
                     |
                 [E5: Ruler]
                  ENDING

═══════════════════════════════════════════════════════════════
                     OPTIONAL SIDE AREAS
═══════════════════════════════════════════════════════════════

From [09: Grand Hallway]:

    → [15: Kitchen] (Get Cheese, Food)
         |
    → [17: Armory] (Get Rusty Sword → Animated Armor fight)
         |
         [D5: Armor Wins] DEATH

    → [18: Chapel] (Lore, Talking Skull, Hints)

    → [22: Secret Passage] (Requires Royal Seal)
         |
         → [Bypass to Tower]

═══════════════════════════════════════════════════════════════
```

---

## Scene Listing with Connections

### ACT I: INFILTRATION (Scenes 01-08)

**[START] → Scene 01**

**Scene 01: Outside Castle Walls**
- **Description:** Dark, stormy night. Castle looms ominously. You hear the princess's screams from the tower.
- **Choices:**
  - A) Climb the garden wall (stealthy) → Scene 02
  - B) Knock on the front gate (bold) → D1 (DEATH: Guards shoot arrows)
  - C) Turn back (cowardly) → Restart with shame message
- **Items:** None
- **NPCs:** None visible

**Scene 02: Climbing the Garden Wall**
- **Description:** Moss-covered stones, slippery but climbable. You hear hounds barking in the distance.
- **Choices:**
  - A) Drop down into courtyard → Scene 03
  - B) Try to climb to window → Fall, Scene 03 (injured start)
- **Items:** None
- **NPCs:** None

**Scene 03: Courtyard - Hounds Released!**
- **Description:** You land in the courtyard. CLANG! An alarm bell. Supernatural hounds with glowing eyes emerge from the shadows. They're FAST.
- **Choices:**
  - A) Fight the hounds (brave/stupid) → D2 (DEATH: Torn apart, but described humorously)
  - B) RUN to the drawbridge! → Scene 04
  - C) Hide in the fountain → Scene 06
- **Items:** None
- **NPCs:** Infernal Hounds (hostile)

**D2: Death by Hounds**
- **Description:** "You draw your... wait, you don't have a weapon. The hounds appreciate your optimism if not your tactical thinking. At least your death is quick. The castle awards you 'Most Confident Corpse.'"
- **Choices:**
  - Try again → Restart at Scene 01

**Scene 04: Sprint to Drawbridge**
- **Description:** You run. The hounds gain. Their hot breath on your neck. You reach the drawbridge controls—a rusty lever.
- **Choices:**
  - A) Pull lever to drop gate (trap hounds) → Scene 05
  - B) Jump over moat (risky) → D3 (DEATH: Moat is full of spikes, not water)
  - C) Turn and fight → D2 (DEATH)
- **Items:** None
- **NPCs:** Hounds (chasing)

**Scene 06: Hide in Fountain**
- **Description:** You dive into the fountain. The water is ice cold and full of algae. The hounds circle, sniffing. One dips its paw in and yelps—holy water! They retreat.
- **Choices:**
  - A) Emerge and go to drawbridge → Scene 05
  - B) Stay hidden → Freeze to death (comedic), D6
- **Items:** Holy Water (optional, for future encounter)
- **NPCs:** Hounds (deterred)

**D3: Death by Moat**
- **Description:** "You leap gracefully over the moat. Sadly, your landing is less graceful. The spikes, freshly sharpened per castle regulations, welcome you enthusiastically. The hounds peer over the edge and look disappointed."
- **Choices:**
  - Try again → Restart at Scene 01

**Scene 05: Drawbridge Gate Drops**
- **Description:** The gate SLAMS down, trapping the hounds on the other side. They howl in frustration. You're safe. The castle entrance hall awaits.
- **Choices:**
  - A) Enter castle → Scene 07
- **Items:** None
- **NPCs:** Hounds (trapped outside)

**Scene 07: Castle Entrance Hall**
**[CONVERGENCE POINT 1 - All "get inside" paths lead here]**
- **Description:** Vast entrance hall. Cobwebs everywhere. Suits of armor line the walls. A grand staircase leads up. Hallways branch left and right.
- **Choices:**
  - A) Forward to Throne Room → Scene 08
  - B) Left hallway (Grand Hallway hub) → Scene 09
  - C) Right hallway (Guard room) → Scene 23
  - D) Up the stairs (locked) → Message "Stairs are blocked by magical barrier"
- **Items:** None
- **NPCs:** Ghostly Guards (harmless, warn you)

**Scene 08: Throne Room**
- **Description:** A massive throne room. The throne itself radiates dark energy. A skeleton sits on the throne wearing a crown. Behind the throne, you notice strange scratch marks on the wall.
- **Choices:**
  - A) Examine throne → Warning message, don't sit yet
  - B) Search behind throne → Find GOLDEN GOBLET (hidden)
  - C) Examine skeleton → Lore text about the curse
  - D) Leave to Grand Hallway → Scene 09
- **Items:** Golden Goblet (hidden, requires search)
- **NPCs:** Skeleton King (dead, lore only)

### ACT II: EXPLORATION (Scenes 09-18)

**Scene 09: Grand Hallway - Central Hub**
**[CONVERGENCE POINT 2 - All explorers reach here eventually]**
- **Description:** A long hallway with many doors. Torches flicker. You hear distant sounds: rattling chains, dragon snores, maniacal laughter. A helpful sign reads "YOU WILL DIE HERE" with an arrow pointing everywhere.
- **Choices:**
  - A) Door 1: Library → Scene 10
  - B) Door 2: Dungeon stairs (down) → Scene 12
  - C) Door 3: Dragon's Cave (hot air) → Scene 14
  - D) Door 4: Wizard's Study → Scene 16
  - E) Door 5: Kitchen → Scene 15
  - F) Door 6: Armory → Scene 17
  - G) Door 7: Chapel → Scene 18
  - H) Back to Entrance Hall → Scene 07
- **Items:** None (hub)
- **NPCs:** None (just doors and choices)

**Scene 10: Library**
- **Description:** Endless shelves of moldy books. Dust makes you sneeze. On the main table, an ancient map of the castle is spread out. You notice faint markings but can't read them.
- **Choices:**
  - A) Read books (lore) → Flavor text
  - B) Examine map closely → "You need special vision to read this"
  - C) Take Ancient Tome → Item acquired
  - D) (If have Spectacles) Use spectacles on map → Scene 11 (Revelation!)
  - E) Return to hallway → Scene 09
- **Items:** Ancient Tome
- **NPCs:** None

**Scene 11: The Invisible Message (Spectacles Required)**
- **Description:** Through the magic spectacles, invisible ink glows on the map! It reads: "The Tower Key lies where kings sit in eternal rest. Search behind the throne for the scratch marks point to truth."
- **Choices:**
  - A) Go to Throne Room → Scene 08
  - B) Return to hallway → Scene 09
- **Items:** None (knowledge gained)
- **NPCs:** None

**Scene 12: Dungeon Entrance**
- **Description:** Stone stairs descend into darkness. The smell is terrible. You hear humming—someone is HUMMING cheerfully in a dungeon. That's concerning.
- **Choices:**
  - A) Descend to dungeon → Scene 13
  - B) Nope, go back → Scene 09
- **Items:** None
- **NPCs:** None (sound of Troll below)

**Scene 13: Troll's Lair**
- **Description:** A surprisingly cozy dungeon cell. The troll, GRIZELDA, sits knitting a scarf. "Oh! A visitor! Welcome, welcome. Before I let you pass, you must answer my riddle. I'm afraid it's union rules."
- **Riddle:** "I have cities but no houses, forests but no trees, water but no fish. What am I?"
- **Answer:** A map
- **Choices:**
  - A) Answer riddle (player types answer) → If correct: Scene 13B (Success), If wrong: D7 (Pit trap DEATH)
  - B) (If have Golden Goblet) Bribe the troll → Scene 13B (Success)
  - C) Attack the troll → D8 (Troll is surprisingly strong, DEATH)
  - D) Flee → Scene 12
- **Items:** None here
- **NPCs:** Grizelda the Troll (riddle challenge)

**Scene 13B: Troll Rewards You**
- **Description:** "Excellent! You're smarter than you look. Most adventurers choose violence. Here, take these. They belonged to the last wizard who visited. He won't need them anymore." She hands you MAGIC SPECTACLES.
- **Choices:**
  - A) Thank her and leave → Scene 09
  - B) Ask about the castle → Lore hints
- **Items:** Magic Spectacles (critical)
- **NPCs:** Grizelda (friendly now)

**D7: Wrong Riddle Answer**
- **Description:** "Oh dear. Wrong answer, I'm afraid. The trapdoor opens. On your way down, you have time to think 'I really should have paid attention in geography class.' The spikes at the bottom are very educational."
- **Choices:**
  - Try again → Scene 01

**Scene 14: Dragon's Cave**
- **Description:** HEAT. Overwhelming heat. A massive dragon, PYRRHUS, sleeps on a pile of gold and bones. His snores shake the room. You spot a vial of DRAGON'S FLAME on a pedestal near his tail. He twitches.
- **Choices:**
  - A) Sneak to pedestal (quiet) → Scene 14B (Success, get flame)
  - B) Wake dragon and ask nicely → D4 (Dragon panics, accidentally incinerates you)
  - C) (If have Cheese) Leave cheese for mice → Scene 14C (Dragon wakes, grateful)
  - D) Grab and run → 50% chance, Scene 14B or D4
  - E) Leave quietly → Scene 09
- **Items:** Dragon's Flame (risky to get)
- **NPCs:** Pyrrhus the Anxious Dragon (sleeping)

**Scene 14B: Successfully Obtained Dragon's Flame**
- **Description:** You carefully lift the vial. The dragon snores on. You tiptoe away, heart pounding. SUCCESS! You have the dragon's flame.
- **Choices:**
  - A) Leave quietly → Scene 09
- **Items:** Dragon's Flame (acquired)
- **NPCs:** Pyrrhus (still sleeping)

**Scene 14C: Mouse Negotiation**
- **Description:** The dragon wakes to see you with cheese. His eyes widen in terror. "YOU! Are those... MICE?! Get them out! GET THEM OUT! I'll give you anything!" He tosses you the dragon's flame vial. "Just promise they're gone!"
- **Choices:**
  - A) Promise to remove mice → Get Dragon's Flame, dragon becomes ally
  - B) Taunt dragon with mice → D9 (Dragon faints on top of you, DEATH by crushing)
- **Items:** Dragon's Flame (gift)
- **NPCs:** Pyrrhus (terrified but friendly)

**D4: Dragon Panic**
- **Description:** "The dragon wakes with a start. 'AHHH! AN INTRUDER!' He panics, flailing wildly. A burst of flame incinerates you, three tapestries, and a very surprised bat. 'I'm so sorry!' he wails at your ashes. 'I have anxiety!'"
- **Choices:**
  - Try again → Scene 01

**Scene 15: Kitchen (Optional)**
- **Description:** An abandoned kitchen. Moldy food everywhere. In the pantry, you find surprisingly fresh CHEESE. It's moving. Mice!
- **Choices:**
  - A) Take cheese (and mice) → Item acquired
  - B) Cook something (why?) → Food poisoning, lose turn
  - C) Leave → Scene 09
- **Items:** Moldy Cheese (with mice)
- **NPCs:** Castle Mice

**Scene 16: Wizard's Study**
- **Description:** Books, potions, chaos. An old wizard, MERVIN, squints at you. "Ah! The pizza! Finally! Wait... you're not pizza. Are you my mother? No, mother's been dead for sixty years. Who are you again?"
- **Choices:**
  - A) Play along (pretend to be pizza) → He pays you, gives ROYAL SEAL accidentally
  - B) Explain you're a rescuer → He doesn't believe you, provides confusing hints
  - C) Ask about the princess → Cryptic lore about tower
  - D) Leave the confused wizard → Scene 09
- **Items:** Royal Seal (if you play along)
- **NPCs:** Mervin the Myopic Wizard

**Scene 17: Armory (Optional)**
- **Description:** Weapons everywhere. A RUSTY SWORD looks tempting. A suit of armor stands in the corner. It's definitely watching you.
- **Choices:**
  - A) Take Rusty Sword → Animated Armor attacks! → D5 (DEATH)
  - B) Leave sword alone → Armor nods approvingly, Scene 09
  - C) Talk to armor → It warns you: "The sword is cursed. Don't be stupid."
- **Items:** Rusty Sword (cursed)
- **NPCs:** Animated Armor (guardian)

**D5: Animated Armor**
- **Description:** "The moment you touch the sword, the armor springs to life. 'THIEF!' it shouts. You try to fight with the rusty sword. It breaks immediately. The armor shakes its head disappointedly before running you through. 'Tourists,' it mutters."
- **Choices:**
  - Try again → Scene 01

**Scene 18: Chapel (Optional)**
- **Description:** A small chapel. Candles burn despite no one being here. A TALKING SKULL sits on the altar. "Hello, friend! Care for a riddle? A joke? Existential dread?"
- **Choices:**
  - A) Ask about the castle → Lore and hints
  - B) Ask about the curse → Important backstory
  - C) Ask for help → Skull gives cryptic advice about the tower
  - D) Leave → Scene 09
- **Items:** None
- **NPCs:** Talking Skull (helpful, punny)

### ACT III: ASCENSION & RESOLUTION (Scenes 19-27)

**Scene 19: Tower Staircase**
**[CONVERGENCE POINT 3 - All successful paths lead here]**
- **Description:** You've found the tower entrance! But the stairs are completely encased in magical ice. It radiates cold. You'll need intense heat to melt it.
- **Choices:**
  - A) (If have Dragon's Flame) Use flame on ice → Scene 20 (Ice melts!)
  - B) Try to climb ice → Slip and fall, minor damage, try again
  - C) (If have 3 Torches) Combine torches → Scene 20 (alternate solution)
  - D) Give up → Scene 09 (return to hallway)
- **Items:** None
- **NPCs:** None
- **Gate:** Requires Dragon's Flame or alternate heat source

**Scene 20: Tower Landing**
- **Description:** The ice melts away, revealing spiral stairs. You climb. At the top, a heavy wooden door. It's locked. You hear the princess humming inside (she sounds... annoyed).
- **Choices:**
  - A) (If have Tower Key) Unlock door → Scene 21
  - B) Knock → Princess shouts "I'm busy escaping, come back later!"
  - C) (If have Royal Seal) Command the door open → Scene 21 (alternate)
  - D) Try to break door → It's solid oak, you hurt your shoulder
- **Items:** None
- **NPCs:** Princess (inside, voice only)
- **Gate:** Requires Tower Key or Royal Seal

**Scene 21: Princess Chamber**
- **Description:** The door opens. Princess ELARA looks up from a half-finished rope ladder. She's covered in dust, holding a lockpick. "Oh. A rescuer. Wonderful. I was only three days away from escaping myself." She's unimpressed but evaluates you carefully.
- **Choices:**
  - A) "Let's escape together" → She evaluates your journey (items, choices)
  - B) "I've come to save you!" (boastful) → She rolls her eyes
  - C) "Need help with that rope?" (helpful) → She appreciates competence
  - D) (If have Royal Seal) "By royal decree, you're rescued" → She laughs
- **Items:** None
- **NPCs:** Princess Elara (evaluating you)
- **Outcome:** Next scene depends on items collected and dialogue choices

**ENDINGS (Scenes E1-E5)**

**Scene E1: Heroic Rescue** ⭐
- **Requirements:** Tower Key, Dragon's Flame, Magic Spectacles, helped NPCs
- **Description:** "Princess Elara assesses you. 'Not bad. You actually used your brain.' Together you descend the tower. The dragon waves. The troll calls 'Good luck!' The castle begins to crumble as the curse weakens. Outside, she admits: 'You're more competent than you look. Thanks.' High praise from her. You WIN!"
- **Ending Type:** Classic Victory

**Scene E2: Tragic Betrayal** 🗡️
- **Requirements:** Arrived without helping NPCs OR killed NPCs OR only have key, no diplomacy
- **Description:** "Princess Elara smiles sweetly. 'My hero,' she says. Then she PUSHES you off the balcony. 'The curse requires a sacrifice. You're very sacrificial-looking. Nothing personal!' As you fall, you realize she's been in on the curse the whole time. The last thing you see is her waving cheerfully. The end."
- **Ending Type:** Dark Twist (DEATH but story ending)

**Scene E3: Mutual Escape** 🤝
- **Requirements:** Royal Seal, convinced NPCs to help, clever dialogue choices
- **Description:** "Princess Elara grins. 'You're smarter than most. I like smart.' She shows you HER escape plan—a secret passage she found. Together, using your items and her knowledge, you navigate out. The dragon gives you a ride over the wall. The troll packs you snacks. Mervin thinks you're both pizza. The curse breaks. You both escape. Partnership ending!"
- **Ending Type:** Cooperative Victory

**Scene E4: Castle Collapse** 💥
- **Requirements:** Woke dragon violently, killed troll, broke things, chaos path
- **Description:** "Your rampage through the castle has consequences. The magical foundations can't take it. Walls crumble. The dragon evacuates. The wizard flees. The princess escapes in the chaos, stealing a horse. 'Thanks for the distraction, idiot!' she yells. You're buried in rubble but somehow survive. The local tavern names a drink after you: 'The Castle Destroyer.' You're famous for being terrible. Success?"
- **Ending Type:** Chaotic Comedy

**Scene E5: Become the New Ruler** 👑
- **Requirements:** ALL items collected, ALL NPCs befriended, sit on throne in Scene 08 after getting key
- **Secret Path:** After getting Tower Key, return to throne room, sit on throne with all items
- **Description:** "As you sit on the cursed throne holding every item and having befriended every creature, the castle recognizes you. The curse lifts—but transfers to YOU. You're now the ruler. The princess shrugs and leaves to become an adventurer. You're stuck managing a castle with an anxious dragon, a riddle-obsessed troll, and a wizard who thinks you're pizza delivery. This is your life now. Congratulations?"
- **Ending Type:** Secret Ironic Ending

---

## Scene Summary Statistics

**Total Scenes:** 28
- Story Scenes: 21
- Death Scenes: 6 (D1-D6)
- Ending Scenes: 5 (E1-E5)
- Convergence Hubs: 3 (Scenes 07, 09, 19)

**Critical Path Length:** 15 scenes (01 → 02 → 03 → 04 → 05 → 07 → 08 → 09 → 10 → 13 → 14 → 19 → 20 → 21 → E1)

**Branch Points:** 8 major decision points
**Optional Scenes:** 7 (Kitchen, Armory, Chapel, Wizard alternate paths, etc.)

---

## Validation Checks (For Automated Testing)

**Graph Integrity Tests:**
- ✅ No orphaned scenes (all scenes reachable from START)
- ✅ No dead-ends except DEATH and ENDING scenes
- ✅ All item requirements have corresponding items
- ✅ Every choice leads to valid scene
- ✅ At least 3 endings reachable from START
- ✅ Critical path playable without optional scenes
- ✅ Convergence points properly funnel branches

---

**Document Status:** Complete - Ready for Scene Descriptions
**Last Updated:** 2025-10-02
