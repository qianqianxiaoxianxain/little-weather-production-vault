# -*- coding: utf-8 -*-
"""
prompts_ep01_little_weather.py
《小天气》第一卷·第一集《晴转多云的铁皮盒》生产级 H3 提示词字典
已完成纯正向提示词重构、声学去 BGM、纯净人话音素标记与道具严密死锁。
"""

PROMPTS = {
    "SHOT_01": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, gentle peach blush on cheeks, two tiny nubby vapor hands, and a single light-blue sprout on top of its head. No animal ears, no tail, no fur.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot under a sunlit grape trellis, <Subject 1> Keke is stuck in a bamboo tray doing a cute sit-up trying to pull its plump bottom out.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for cloud shape, eyes, sprout, and white vapor texture.

detailed_description:
Cinematic 3D animation 16:9 widescreen composition under a lush green grape trellis in a cozy red-brick courtyard. Dappled May midday sunlight filtering through translucent grape leaves onto an ancient woven bamboo sun-drying tray.
From 0.0s to 2.5s, 15cm chubby cloud creature Keke lies in a groove of the bamboo tray, its round bottom snugly stuck; Keke puffs its rosy cheeks and vigorously pulls its upper body upward into a cute, comical sit-up.
From 2.5s to 5.0s, Keke's soft milky-white body quivers three times like a fluffy dumpling as it strains to pop its bottom out, failing comically; it rests with tiny nubby hands propped on the bamboo slats, panting softly, its blue head-sprout leaning forward.
Pixar-Ghibli warm textures, crisp 24fps motion.

overall_soundscape:
Gentle summer breeze rustling grape leaves, light creak of natural bamboo weaving, soft strained cloud breathing "gu... en!", and peaceful quiet yard ambience. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_02": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, gentle peach blush on cheeks, two tiny nubby vapor hands, and a single light-blue sprout on top of its head. No animal ears, no tail, no fur.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, <Subject 1> Keke accidentally condenses a miniature storm cloud above its head that drops a tiny hailstone right onto its forehead.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for cloud body, facial expression, and sprout.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up in the sunlit bamboo tray under grape leaves.
From 0.0s to 2.5s, Keke sits stuck in the bamboo groove, cheeks puffed indignantly; two inches above its blue sprout, a palm-sized dark grey thundercloud suddenly condenses with a soft pop, and a single pea-sized translucent ice hailstone drops straight down, bonking directly onto Keke's forehead with a tiny bounce.
From 2.5s to 5.0s, Keke's dark indigo eyes widen in comically stunned disbelief for one second, then tear up with soft pink flush; Keke clutches its forehead sprout with both chubby nubby hands, kicking its tiny feet in dramatic squeaky protest.
Pixar-Ghibli warm lighting, crisp 24fps motion.

overall_soundscape:
Subtle condensation pop, crisp "clack" of tiny hail bonking soft cloud forehead, miniature ice pellet rolling on bamboo wood, and Keke's prolonged, adorable aggrieved squeak "guuu---!". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_03": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments. Single character in focus.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, 8-year-old <Subject 1> A Ning crouches on a small red plastic stool, her eyes widening into sparkling wonder as she softly gasps: "哇！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for facial features, pigtails, flower ties, and expressive acting.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up in the sun-dappled courtyard. Warm golden morning sunlight catching flyaway strands of dark hair against lush green vine bokeh.
From 0.0s to 2.5s, 8-year-old A Ning rests her elbows on her knees on the red stool, leaning forward, her big expressive dark eyes suddenly widening with awe, sparkling highlights dancing in her pupils as her mouth opens in pure childlike wonder.
From 2.5s to 5.0s, she gently presses both palms against her flushed rosy cheeks in pure joy, her lips forming a crisp, soft exclamation as she speaks her line: "<d>[Chinese] 哇！</d>". Her eyebrows rise with gentle excitement.
Pixar-Ghibli warm skin subsurface scattering, crisp 24fps motion.

overall_soundscape:
Gentle outdoor courtyard atmosphere, soft rustle of child's cotton sleeves, and A Ning's crystal-clear, pure child vocalization: "<d>[Chinese] 哇！</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_04": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head.
<Subject 2> is the rescue prop: a large stainless steel slotted noodle spoon lined with a single dry paper napkin patterned with cute red strawberries, held steadily by gentle child hands on the right.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot, <Subject 2> the large slotted spoon lined with strawberry napkin gently lands on the bamboo tray beside <Subject 1> Keke, who curiously inspects it.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2>.
<Subject 2>: realistic stainless steel utensil and paper napkin texture.

detailed_description:
Cinematic 3D animation 16:9 widescreen composition on the woven bamboo tray.
From 0.0s to 2.5s, the large round stainless steel slotted spoon lined with a cheerful red-strawberry-patterned paper napkin descends gently from the right like a spaceship, resting flush against the bamboo slats beside stuck Keke.
From 2.5s to 5.0s, Keke stops rubbing its head sprout, tilts its puffy white body sideways with inquisitive eyes, and cautiously reaches out one tiny round vapor foot to tap the edge of the strawberry napkin testing its stability.
Pixar-Ghibli natural lighting, metallic gleam, crisp 24fps motion.

overall_soundscape:
Soft metallic "clink" of the steel spoon resting against bamboo wood, gentle rustle of dry paper napkin in the summer breeze, and quiet courtyard bird chirp. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_05": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments. Single character in focus.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, <Subject 1> A Ning holds the spoon handle and gives a playful countdown ultimatum, speaking: "二点八！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for face, pigtails, and comedic acting.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up in the cozy garden patio.
From 0.0s to 2.2s, 8-year-old A Ning crouches holding the wooden end of the spoon handle, furrowing her brow in mock-serious teacher fashion, counting down silently with her fingers.
From 2.2s to 5.0s, seeing the cloud still hesitating, she leans in slightly, her eyes narrowing with mischievous humor as she delivers her rapid deadline line: "<d>[Chinese] 二点八！</d>". Her mouth twitches with an adorable suppressed giggle.
Pixar-Ghibli warm lighting, crisp 24fps motion.

overall_soundscape:
A Ning's clear, lively, humorous whisper-shout: "<d>[Chinese] 二点八！</d>", followed by quiet garden courtyard atmosphere. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_06": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head. No animal ears, no tail, no fur.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, <Subject 1> Keke rushes onto the strawberry paper napkin in the slotted spoon, slips comically, and falls flat on its back like a soft mochi dumpling.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for elastic cloud physics and funny expressions.

detailed_description:
Cinematic 3D animation 16:9 widescreen top-down close-up inside the round slotted spoon.
From 0.0s to 2.5s, hurried by the countdown, Keke pulls its bottom free and takes a hasty step onto the smooth dry strawberry-patterned paper napkin; its tiny round cloud foot instantly slips forward, legs pinwheeling hilariously in mid-air.
From 2.5s to 5.0s, Keke lands flat on its rounded back with a soft, squishy mochi-like bounce right in the middle of the red strawberry print, its tiny stubby hands and feet sticking straight up in the air, completely frozen in shock.
Pixar-Ghibli playful lighting, crisp 24fps motion.

overall_soundscape:
Quick paper slip squeak, soft elastic "plop" landing sound like a dropped mochi, Keke's tiny startled squeak "o-yo!", followed by a deadpan 1.5-second comic silence. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_07": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, light-blue sprout on head.
<Subject 2> is the slotted spoon lined with the strawberry napkin, lifted steadily by gentle child hands.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up tracking shot, <Subject 1> Keke blushes bright pink in embarrassment and starts raining a tiny localized shower onto the napkin as the spoon is lifted.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2>.
<Subject 2>: realistic paper napkin wetting simulation and stainless steel reflections.

detailed_description:
Cinematic 3D animation 16:9 widescreen tracking shot moving upward.
From 0.0s to 2.5s, lying on its back in the spoon, Keke's cheeks and sprout flush intensely bright cherry-pink with pure embarrassment; it covers its eyes with both nubby hands, and its underside abruptly unleashes a teacup-sized miniature rain shower, drenching the strawberry napkin with tiny clear raindrops.
From 2.5s to 5.0s, gentle child hands carefully lift the long-handled spoon upward off the bamboo tray into the warm sunlight, carrying the blushing, softly dripping little cloud upwards into safety.
Pixar-Ghibli liquid micro-physics, crisp 24fps motion.

overall_soundscape:
Crisp miniature raindrops pitter-pattering on paper napkin "shhh-shhh", gentle paper dampening sound, Keke's muffled embarrassed cloud whining "wu-wu-wu...", and soft lifting air movement. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_08": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments.
<Subject 2> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head.

summary:
[reference generation] In a 5.0-second 16:9 widescreen macro close-up shot in a cozy bedroom, <Subject 1> A Ning gently pokes <Subject 2> Keke's squishy cheek like milk pudding and softly comforts: "别怕呀。".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1>.
<Subject 2>: fully_preserved from <Picture 2> for elastic pudding deformation.

detailed_description:
Cinematic 3D animation 16:9 widescreen macro close-up on the bedroom floor foam mat. Soft diffused window daylight.
From 0.0s to 2.5s, 8-year-old A Ning extends her gentle chubby child forefinger, pressing softly into Keke's puffy white cheek; the cloud surface yields smoothly like fresh warm milk pudding with an adorable dimple, bouncing back elastically as she retracts her finger.
From 2.5s to 5.0s, Keke blinks its dark indigo eyes in stunned surprise, while A Ning smiles with immense tenderness, speaking softly in reassuring child tones: "<d>[Chinese] 别怕呀。</d>".
Pixar-Ghibli tactile squish physics, crisp 24fps motion.

overall_soundscape:
Subtle squishy pudding rebound sound, quiet bedroom indoor silence, and A Ning's soft, warm reassuring whisper: "<d>[Chinese] 别怕呀。</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_09": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head. No animal ears, no tail, no fur.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, <Subject 1> Keke stands with tiny hands on hips and emits a harmless, kitten-purr static electricity spark from its cheek.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for facial expression and micro-electric visual effects.

detailed_description:
Cinematic 3D animation 16:9 widescreen macro close-up in the cozy bedroom.
From 0.0s to 2.5s, Keke snaps upright like a feisty kitten, putting both tiny nubby vapor hands on its chubby hips; its sprout bristling cutely, a hairline-thin, harmless violet-gold static spark "zaps" across the gap towards the child's retreating fingertip.
From 2.5s to 5.0s, as the child's hand pulls back with a playful chuckle, Keke puffs out its chest proudly and purrs with a vibrating throat hum like a satisfied kitten, its sprout rocking with triumphant glee.
Pixar-Ghibli lighting, subtle glow on vapor edges, crisp 24fps motion.

overall_soundscape:
Delicate winter sweater static "snap" (crisp and harmless), Keke's deep vibrating kitten-like throat purr "gulu-gulu-gulu", and child's amused chuckle. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_10": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head.
<Subject 2> is A Ning (阿宁), seated on the right in over-the-shoulder perspective, dark pigtails visible.

summary:
[reference generation] In a 5.0-second 16:9 widescreen over-the-shoulder shot, <Subject 1> Keke scratches its sprout trying to recall where it came from, sighing out a gentle puff of white mist.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2>.
<Subject 2>: fully_preserved from <Picture 1>.

detailed_description:
Cinematic 3D animation 16:9 widescreen over-the-shoulder framing in the peaceful bedroom.
From 0.0s to 2.5s, Keke sits on the damp napkin, scratching its light-blue sprout with one chubby nubby hand; its dark indigo eyes look up at the ceiling in deep, childlike confusion, searching its blank memories.
From 2.5s to 5.0s, unable to remember, Keke lets out a gentle, quiet sigh, exhaling a small swirl of translucent sweet white mist from its mouth that curls peacefully through the sunlit bedroom air before dissolving.
Pixar-Ghibli soft atmospheric haze, crisp 24fps motion.

overall_soundscape:
Gentle, quiet exhalation of cloud vapor "whooosh...", faint peaceful whisper of room air, and distant tranquil outdoor birdsong. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_11": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments. Single character in focus.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, 8-year-old <Subject 1> A Ning points playfully and giggles her hilarious line: "像张小胖出汗！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for cheerful expression, pigtails, and comedic timing.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up in the bright afternoon bedroom.
From 0.0s to 2.2s, 8-year-old A Ning sits cross-legged on the floor cushion, looking down at the wet napkin before suddenly brightening up as if discovering a hilarious epiphany, pointing her finger with playful delight.
From 2.2s to 5.0s, adorable dimples appear on her cheeks as she tilts her head and delivers her iconic teasing line with crisp comedic rhythm: "<d>[Chinese] 像张小胖出汗！</d>". She immediately bursts into sweet, uncontrollable giggles, her shoulders bobbing joyfully.
Pixar-Ghibli lively child animation, crisp 24fps motion.

overall_soundscape:
A Ning's cheerful, lively, crystal-clear child teasing voice: "<d>[Chinese] 像张小胖出汗！</d>", followed by genuine, innocent child laughter. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_12": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, light-blue sprout on head.
<Subject 2> is the slotted spoon and wet strawberry napkin.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, <Subject 1> Keke turns slate-blue with dramatic sorrow and unleashes a miniature weeping rain shower onto the spoon.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for facial expression and fluid color-shift weather dynamics.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up on the bedroom floor cushion.
From 0.0s to 2.5s, devastated by being compared to sweaty classmate Zhang Xiaopang, Keke's milky-white color instantly shifts into a melancholy slate-blue; giant watery cartoon tears well up in its dark indigo eyes as it covers its face with both chubby nubby hands.
From 2.5s to 5.0s, its underside abruptly unleashes a dramatic, localized miniature rain shower splashing onto the soaked strawberry napkin below, billowing faint sweet misty steam with the fresh scent of summer grass.
Pixar-Ghibli expressive weather physics, crisp 24fps motion.

overall_soundscape:
Sudden rushing miniature summer downpour "shhh-splatter", tiny raindrops drumming vigorously on the damp paper napkin, and Keke's adorable, muffled sniffles "wu-wu-wu...". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_13": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, light-blue sprout on head. No animal ears, no tail, no fur.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, the quiet room is interrupted as <Subject 1> Keke's tummy lets out a comical, reverberant frog-like rumble, causing Keke to instantly turn away in shame.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for elastic belly vibration and blushing turnaround.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up inside the peaceful bedroom.
From 0.0s to 2.0s, the weeping rain instantly cuts off; Keke tries to cross its tiny arms and act haughty, while the bedroom is completely dead silent with the rhythmic tick of a wall clock.
From 2.0s to 5.0s, Keke's plump white cloud tummy abruptly ripples with a deep, comical acoustic vibration like a hungry frog croak; Keke's cheeks flash incandescent crimson in pure mortification as it instantly whirls 180 degrees away from the camera, curling into a tight, motionless ball of shame.
Pixar-Ghibli comedic timing, crisp 24fps motion.

overall_soundscape:
Two crisp rhythmic wall clock ticks "tick... tock...", followed by an astonishingly loud, comical, hollow tummy rumble "gulu-croooak!", and a tiny squeak of shame. Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_14": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments. Single character in focus.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot, <Subject 1> A Ning saves the cloud's dignity by patting her own tummy and shouting proudly: "是我肚子叫！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for warm maternal/sisterly emotion and energetic acting.

detailed_description:
Cinematic 3D animation 16:9 widescreen medium shot on the cozy bedroom floor mat.
From 0.0s to 2.2s, 8-year-old A Ning pauses tenderly upon seeing the cloud curl up in mortification; instead of laughing, a warm, protective beam spreads across her face as she boldly slaps both palms onto her own soft belly twice with loud, cheerful thumps.
From 2.2s to 5.0s, she puffs out her chest chivalrously and declares at the top of her lungs with bright, unwavering loyalty: "<d>[Chinese] 是我肚子叫！</d>". Her eyes radiate pure, reassuring warmth.
Pixar-Ghibli heartwarming character performance, crisp 24fps motion.

overall_soundscape:
Two crisp, hollow slaps of child palms on clothing/belly "pat-pat!", followed by A Ning's loud, proud, resonant child shout: "<d>[Chinese] 是我肚子叫！</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_15": """subject_definitions:
<Subject 1> is the Little Yellow Duck thermos bottle: a bright daffodil-yellow children's stainless steel thermos with an adorable duck-bill flip lid and smooth glossy finish.
<Subject 2> is gentle child hands popping open the lid from the right.

summary:
[reference generation] In a 5.0-second 16:9 widescreen macro close-up shot on a wooden desk, <Subject 2> child hands click open <Subject 1> the yellow duck thermos, releasing fragrant golden swirls of lemon-honey steam.

retention_analysis:
<Subject 1>: sharp product details, realistic plastic spring latch and stainless steel interior.
<Subject 2>: child hand scale and natural interaction.

detailed_description:
Cinematic 3D animation 16:9 widescreen macro close-up on the warm wooden desk surface. Warm afternoon sunbeams catching dust motes in the background.
From 0.0s to 2.0s, child fingers press the latch on the bright yellow duck thermos bottle; with a crisp mechanical snap, the duck-head spring lid pops wide open.
From 2.0s to 5.0s, thick, swirling plumes of warm, translucent milky-white steam billow upward from the steaming hot lemon-honey water inside, catching golden backlighting and swirling gracefully through the air toward the left.
Pixar-Ghibli fluid steam dynamics, crisp 24fps motion.

overall_soundscape:
Crisp spring-loaded latch release "click-snap!", soft air puff as lid springs open, and the faint, delicate thermal steam hiss "hiss...". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_16": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head.
<Subject 2> is the bright yellow duck thermos bottle steaming on the right.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot, <Subject 1> Keke pretends to casually wander by before greedily inhaling the warm lemon steam, swelling back into a plump, radiant cloud.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> with expansion swelling dynamics.
<Subject 2>: matching <Subject 1> thermos from previous shot.

detailed_description:
Cinematic 3D animation 16:9 widescreen composition across the polished wooden desk.
From 0.0s to 2.5s, Keke pretends to look innocently at the ceiling, slowly waddling backwards step-by-step toward the yellow thermos, its eyes furtively glancing sideways at the rising sweet steam.
From 2.5s to 5.0s, reaching the rim, Keke suddenly opens its tiny round mouth wide, inhaling the thick white lemon steam like a powerful miniature vacuum; its dry, crumpled vapor body instantly rehydrates, swelling by 25% into a delightfully plump, bouncy, radiant pearl-white mochi ball.
Pixar-Ghibli volumetric steam simulation, crisp 24fps motion.

overall_soundscape:
Subtle squeaky cloud steps on smooth wood, followed by a massive, hilarious vacuum inhalation whoosh "whoooosh-gulp!", and a deeply contented, squeaky cloud exhale "haaa~". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_17": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, dark indigo oval eyes, peach blush on cheeks, two tiny nubby vapor hands, light-blue sprout on head.
<Subject 2> is A Ning (阿宁), seated on the right smiling gently, 100% identical to <Picture 1>.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot, a glowing ping-pong-sized sun pops out of <Subject 1> Keke's head, which Keke panics to shove back down while <Subject 2> A Ning covers for it: "窗户反光呢！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> with volumetric miniature sun emission.
<Subject 2>: fully_preserved from <Picture 1>.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up on the sunlit desk.
From 0.0s to 2.5s, filled with sweet warm water, Keke's sprout suddenly pops open with a joyful "bop!", and a glowing, radiant miniature golden sun the size of a ping-pong ball emerges, casting warm amber light across the wooden tabletop.
From 2.5s to 5.0s, Keke gasps in utter panic, frantically using both chubby cloud hands to shove and squash the glowing little sun back into its head; in the background, A Ning covers her mouth suppressing a giggle and playfully says: "<d>[Chinese] 窗户反光呢！</d>".
Pixar-Ghibli radiant lighting and comedic acting, crisp 24fps motion.

overall_soundscape:
Bouncy rubber pop "bop!", gentle radiant warm hum of sunlight, frantic squishy slapping sounds as Keke pushes the sun down, and A Ning's clear, comforting child line: "<d>[Chinese] 窗户反光呢！</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_18": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments.
<Subject 2> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>.
<Subject 3> is the iconic Danish butter cookie tin: a round royal-blue metal tin with elegant gold embossed patterns, lined neatly with a soft baby-blue cotton cloth napkin.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot, <Subject 2> Keke happily hops into <Subject 3> the blue cookie tin lined with baby-blue cloth, while <Subject 1> A Ning smiles and names it: "叫你可可吧！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1>.
<Subject 2>: fully_preserved from <Picture 2>.
<Subject 3>: accurate royal-blue cookie tin with gold lettering and baby-blue cotton cloth.

detailed_description:
Cinematic 3D animation 16:9 widescreen composition on the cozy study desk.
From 0.0s to 2.5s, 8-year-old A Ning pushes forward the round royal-blue Danish butter cookie tin lined with a clean baby-blue folded cotton napkin; Keke's eyes light up, and it takes a joyful little leap directly into the tin, snuggling down into the soft cotton folds like a king on a plush throne.
From 2.5s to 5.0s, A Ning rests her chin in both hands beside the tin, her dark eyes sparkling with boundless affection as she proudly pronounces its new name: "<d>[Chinese] 叫你可可吧！</d>".
Pixar-Ghibli warm domestic warmth, crisp 24fps motion.

overall_soundscape:
Muffled metal tin settling with a soft "thud" on wood, gentle rustle of clean cotton fabric, and A Ning's tender, sweet, crystal-clear naming line: "<d>[Chinese] 叫你可可吧！</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_19": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to the 8-year-old girl in <Picture 1>. A sweet lively 8-year-old Asian schoolgirl with big sparkling dark brown eyes, chubby rosy cheeks, wearing a clean summer short-sleeve shirt with neat hair. Smooth dark brown human hair with neat bangs, styled in double low curly pigtails tied with white flower scrunchies. Smooth pure human hair with ZERO extra ornaments.
<Subject 2> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>.
<Subject 3> is the blue Danish cookie tin with baby-blue cotton napkin.

summary:
[reference generation] In a 5.0-second 16:9 widescreen macro close-up shot, <Subject 1> A Ning's pinky finger hooks with <Subject 2> Keke's tiny cloud finger in a sacred secret promise, whispering: "拉钩不许说！".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1>.
<Subject 2>: fully_preserved from <Picture 2> for tender finger contact physics.

detailed_description:
Cinematic 3D animation 16:9 widescreen macro close-up at the rim of the blue cookie tin.
From 0.0s to 2.5s, sitting comfortably on the baby-blue cotton napkin, Keke extends its chubby nubby cloud hand, gently hooking its soft vapor pinky around 8-year-old A Ning's extended child pinky finger in a tender, sacred pinky promise.
From 2.5s to 5.0s, their hooked pinkies rock gently twice as A Ning leans in with solemn childlike sincerity, whispering her sacred pact: "<d>[Chinese] 拉钩不许说！</d>". Keke firmly bobs its head, its blue sprout nodding in resolute agreement.
Pixar-Ghibli micro-contact physics and emotional tenderness, crisp 24fps motion.

overall_soundscape:
Extremely gentle, delicate rustle of skin touching soft cotton vapor, and A Ning's solemn, pure whispered promise: "<d>[Chinese] 拉钩不许说！</d>". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

    "SHOT_20": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to the living cloud entity in <Picture 2>. A 15cm chubby spherical cloud being made of soft condensed milky-white vapor, smooth matte texture like warm steamed mochi, seen from the back, showing its round white head and light-blue head sprout.
<Subject 2> is A Ning (阿宁), softly blurred in the right background smiling tenderly, 100% identical to <Picture 1>.
<Subject 3> is the round blue cookie tin with baby-blue cotton napkin.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up shot from behind, a tiny thumb-length miniature rainbow arches up secretly behind <Subject 1> Keke's head before tucking behind its sprout.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 2> for cloud back texture and sprout.
<Subject 2>: fully_preserved from <Picture 1>.

detailed_description:
Cinematic 3D animation 16:9 widescreen close-up shot looking at Keke from behind in the cookie tin. Extremely subtle slow pull-back camera motion.
From 0.0s to 2.5s, sitting on the baby-blue cotton napkin, Keke turns its head away playing aloof; right behind its round fluffy white head, a thumb-length (4cm), crystal-clear, translucent miniature seven-color rainbow arches up like a delicate bridge, sparkling with soft magical iridescence.
From 2.5s to 5.0s, as A Ning smiles with gentle wonder in the soft bokeh background, the bashful tiny rainbow shimmers and gently tucks itself away behind the light-blue head sprout, while Keke's sprout bobs with secret joy.
Pixar-Ghibli poetic closing frame, crisp 24fps motion.

overall_soundscape:
Faint summer breeze rustling sheer window curtains, a delicate, crystal-clear wind chime shimmer "ting...", and Keke's softest, contented little sigh "gu~". Absolutely ZERO BGM, ZERO music, ZERO electronic synthesizer sounds.

non_diegetic_music:
N/A""",

}

if __name__ == "__main__":
    print(f"Loaded {len(PROMPTS)} shots for Little Weather S01E01.")
    for k, v in PROMPTS.items():
        print(f"[{k}] length: {len(v)} chars")