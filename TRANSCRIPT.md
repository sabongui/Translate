# Audio Message from Wadid Sabongui 2: transcript

- **Source file:** `Audio_Message_from_wadid_sabongui_2.m4a` (about 1 min 26 s, mono, one speaker)
- **Language:** Egyptian Arabic, with a few Modern Standard Arabic (formal) phrases
- **Method:** Whisper large-v3 run locally (see [How this was made](#how-this-was-made)), then checked and corrected by hand. Lines marked **[?]** are uncertain.

Pronunciation key: `'` before a vowel is a catch in the throat (Arabic ع "ain", or the Egyptian way of saying ق); `kh` like Scottish "loch"; `gh` like a French "r"; doubled letters are held longer.

## Line by line

| Time | Arabic | How it sounds | English |
|---|---|---|---|
| 0:07 | السلام عليكم يا أخ يوسف | Es-salamu 'alaikum, ya akh Youssef. | Peace be upon you, brother Youssef. |
| 0:14 | أنا مصري قبطي | Ana Masri 'Ebti. | I'm an Egyptian Copt. |
| 0:18 | وبتكلم شوية عربي لغاية النهاردة | W-batkallem shwayyet 'Arabi le-ghayet en-naharda. | And I still speak a little Arabic to this day. |
| 0:26 | للأسف مع الوقت أنا نسيت | Lel-asaf, ma'a el-wa't ana neseet | Unfortunately, over time I've forgotten |
| 0:31 | شوية من اللغة العربية اللي كبرت واتربيت عليها | shwayya men el-logha el-'Arabeyya elli kebert w-etrabbeit 'aleiha. | some of the Arabic I grew up with and was raised on. |
| 0:41 | يشرفني أن أشتغل معاك | Yesharrafni an ashtaghal ma'ak | It would be an honor for me to work with you |
| 0:47 | وأن أقوم بدور الإمام | wa an a'oom be-dawr el-imam. | and to take on the role of the imam. |
| 0:52 | أو أن أشتغل معاك وأن ألعب دور الإمام | Aw an ashtaghal ma'ak wa an al'ab dawr el-imam. | Or rather, to work with you and play the role of the imam. |
| 1:02 | علشان كده عايز أكون صريح | 'Alashan keda 'ayez akoon sareeh | That's why I want to be frank |
| 1:06 | وصادق معاك من الأول | w-sade' ma'ak men el-awwel. | and honest with you from the start. |
| 1:15 | أو، [إن شئت؟] من البداية **[?]** | Aw, [en shi't?] … men el-bedaya. **[?]** | Or, [if you like,] from the very beginning. **[?]** |

## Full English translation

> Peace be upon you, brother Youssef. I'm an Egyptian Copt, and I still speak a little Arabic to this day. Unfortunately, over time I've forgotten some of the Arabic I grew up with and was raised on. It would be an honor for me to work with you and to take on the role of the imam, or rather, to work with you and play the role of the imam. That's why I want to be frank and honest with you from the start, or, if you like, from the very beginning.

## Notes

- **"Masri 'Ebti" (مصري قبطي):** Egyptians usually say ق as a catch in the throat, so *qibti* (Copt) comes out *'ebti*. Whisper wrote it the way it sounds (ابطي); the meaning is "Coptic", i.e. an Egyptian Christian.
- **Formal phrasing:** "Yesharrafni an ashtaghal… wa an a'oom be-dawr…" mixes formal Arabic (*an*, *a'oom*) with Egyptian words (*ashtaghal*, *ma'ak*). He then rephrases with the more everyday *al'ab dawr* ("play the role").
- **"The role of the imam":** this reads like an actor talking to a director or producer about playing an imam, but the message itself doesn't say that. Treat that as a guess.
- **Last line (1:15–1:19):** the least certain part. Whisper gave a different version on each pass: "أو، إذا أردت" ("or, if you want"), "أو سي تو فيو" (nonsense), and in English mode "Or if you want, from the beginning." *Men el-bedaya* ("from the beginning") came up every time; the words before it did not. It is probably a filler such as "or, if you like" or "or rather". Please check this line by ear.
- Timestamps are approximate (to within a second or two).

## How this was made

1. Converted the m4a to 16 kHz mono WAV with `ffmpeg`, and found the pauses with ffmpeg's `silencedetect` filter.
2. Ran OpenAI's Whisper large-v3 (the int8 ONNX build published by the [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) project) on CPU with `scripts/transcribe.py`, in several overlapping windows, since Whisper only sees 30 seconds at a time.
3. Compared the passes. On short clips that were mostly silence, Whisper made up text that wasn't spoken ("تحليل الماء", "ترجمة نانسي قنقر"). This is a known Whisper failure, and those outputs were thrown away. The longer windows agreed with each other and are what the table uses.
4. Wrote the pronunciation and the English translation by hand from the corrected Arabic.

To reproduce:

```sh
pip install sherpa-onnx soundfile
curl -LO https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-large-v3.tar.bz2
tar xjf sherpa-onnx-whisper-large-v3.tar.bz2
ffmpeg -i input.m4a -ac 1 -ar 16000 speech.wav
python3 scripts/transcribe.py speech.wav sherpa-onnx-whisper-large-v3 0,25,46,69.3,86 ar
```
