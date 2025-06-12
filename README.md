# Botpic Generator
Desktop app for generating Telegram botpics (avatars)

### Usage
```sh
botpic gen <emoji> <main_color> [additional_colors ...]
```

### Examples

<div style="
display: flex; flex-direction: row;
gap: 1em; height: fit-content; margin-bottom: 2em;
">
<div style="width: 70%">
<blockquote>Emoji on black background</blockquote>
<br>
<pre>
<code>botpic gen books 000000</code>
</pre>
</div>
<img src="examples/books_000000.png" style="width: 30%"/>
</div>

<div style="
display: flex; flex-direction: row;
gap: 1em; height: fit-content; margin-bottom: 2em
">
<img src="examples/smirking-face_ffffff.png" style="width: 30%"/>
<div style="width: 70%">
<blockquote>Emoji on gradient background</blockquote>
<br>
<pre>
<code>botpic gen smirking-face ffffff d3fad6 d1efb5 edeba0 c3c48d 928c6f</code>
</pre>
</div>
</div>

<div style="
display: flex; flex-direction: row;
gap: 1em; height: fit-content; margin-bottom: 2em
">
<div style="width: 70%">
<blockquote>Emoji with more gradient drops</blockquote>
<br>
<pre>
<code>botpic gen telephone 003049 d62828 f77f00 fcbf49 eae2b7 76818e --drops 1000</code>
</pre>
</div>
<img src="examples/telephone_003049.png" style="width: 30%"/>
</div>

<div style="
display: flex; flex-direction: row;
gap: 1em; height: fit-content; margin-bottom: 2em
">
<img src="examples/printer_4a4063.png" style="width: 30%"/>
<div style="width: 70%">
<blockquote>Emoji scaled to 2x (default 1.5x)</blockquote>
<br>
<pre>
<code>botpic gen printer 4a4063 4a4063 bfacc8 a8c69f 783f8e 4f1271 -s 2</code>
</pre>
</div>
</div>