<div align="center">
	<h1>Loggaby-py</h1>
	<blockquote align="center">🐍 Simple, minimal logging for Python without useless features.</blockquote>
	<p>
		<a href="https://github.com/Loggaby/Loggaby-py/blob/master/LICENSE">
			<img alt="GitHub license" src="https://img.shields.io/github/license/Loggaby/Loggaby-py?style=for-the-badge">
		</a>
		<a href="https://github.com/Loggaby/Loggaby-py/stargazers">
			<img alt="GitHub stars" src="https://img.shields.io/github/stars/Loggaby/Loggaby-py?style=for-the-badge">
		</a>
		<br>
		Loggaby-py is a direct port (aims to be, anyway) of the <a href="https://github.com/Loggaby/Loggaby">original JS</a> version. It does 1 thing and does it well: posting nice logs to a terminal. Or perhaps a file? Anywhere you need can be done with a Transport (not present in this Python version as yet).
		<br><br>
		Oh, it looks like this:<br>
		<img alt="Preview" src="https://modeus.is-inside.me/V6nRi6i6.png">
		<br>
		<i>(Exactly like the original)</i>
	</p>
</div>

# Table of Contents
- [Install](#install)
- [Examples](#examples)
- [Docs](#documentation)
- [License](#license) 

## Install
`pip install loggaby`

## Examples
[Provided Here](examples/).

# Documentation
#### Loggaby(debug=False, levels=[]) 
The Loggaby constructor, which creates a `logger` instance.
  - `debug` {Boolean} Whether to print debug messages. (Default: `True`)
  - `levels` Additional custom levels to provide. (An array of `dict`s)
	- `name` {str} Name of the level that appears in the logs
	- `color` {str} Color of the `name` (accepted values are [these](https://github.com/Luvella/AnsiKit#colors) or a hex value)
	- `debug` {bool} Whether this is a debug log (that is hidden with `debug: false`)
	- `fatal` {bool} Whether to make the level name and message bold and underline
	- `call` {str} Name of the function to use this level

## Levels
`debug`, `log`, `warn`, `error`, `fatal` by default.  

You can log with `logger.<Level>()`. ([examples](#examples))

# License
Loggaby-py is licensed under the MIT license.  
[Read here](LICENSE) for more info.

<hr>
<p align="center">
	<i>A <a href="https://github.com/Luvella">Luvella</a> project.</i>
	<br>
	<img src="https://modeus.is-inside.me/ZvFTbWcA.png" width=52>
</p>
