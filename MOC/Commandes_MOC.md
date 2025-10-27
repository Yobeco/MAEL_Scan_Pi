# Commandes MOC

[mocp - Man Page](https://www.mankier.com/1/mocp#)

Music On Console (audio player)

Examples (TL;DR)

- Launch the MOC terminal UI: `mocp`
- Launch the MOC terminal UI in a specific directory: `mocp path/to/directory`
- Start the MOC server in the background, without launching the MOC terminal UI: `mocp [-S|--server]`
- Add a specific song to the play queue while MOC is in the background: `mocp [-q|--enqueue] path/to/audio_file`
- Add songs recursively to the play queue while MOC is in the background: `mocp [-a|--append] path/to/directory`
- Clear the play queue while MOC is in the background: `mocp [-c|--clear]`
- Play or stop the currently queued song while MOC is in the background: `mocp --play|stop`
- Stop the MOC server while it's in the background: `mocp [-x|--exit]`

[tldr.sh](https://tldr.sh/)

Synopsis

```
**mocp** [Options] [*FILE*|*DIR* ...]
```

Description

MOC is a console audio player with simple ncurses interface.  It supports OGG, WAV, MP3 and other formats.  Just run **mocp**, go to some directory using the menu and press enter to start playing  the file.  The program will automatically play the rest of the files in  the directory.

With no options and no file arguments the program begins in current directory, or in **MusicDir** if the **StartInMusicDir** option is set in the configuration file.  If you give a directory on  the command line, MOC will try to go there.  If a playlist is given,  then it is loaded. With multiple files, playlists or directories,  everything will be added to the playlist recursively (including the  contents of any playlist given). (Note that relative paths in playlists  are resolved with respect to the directory of the playlist, or of the  symlink being used to reference it.)

Options

If an option can also be set in the configuration file the command line overrides it (but see the **[-O](https://www.mankier.com/1/mocp#-O)** option for the list-valued configuration file options exception).

- [-D](https://www.mankier.com/1/mocp#-D),  [--debug](https://www.mankier.com/1/mocp#--debug)

  Run MOC in debug mode.  The client and server log a lot of information to  debug files.  Don't use this; the server log is large.  This is only  available if MOC was compiled without **--disable-debug**.

- [-S](https://www.mankier.com/1/mocp#-S),  [--server](https://www.mankier.com/1/mocp#--server)

  Run only the server and exit.

- [-F](https://www.mankier.com/1/mocp#-F),  [--foreground](https://www.mankier.com/1/mocp#--foreground)

  Implies **[-S](https://www.mankier.com/1/mocp#-S)**.  Run the server in foreground and log everything to stdout.

- [-R](https://www.mankier.com/1/mocp#-R) *NAME*[**:**...], [--sound-driver](https://www.mankier.com/1/mocp#--sound-driver) *NAME*[**:**...]

  Use the specified sound driver(s).  They can be **OSS**, **ALSA**, **JACK**, **SNDIO** or **null** (for debugging).  Some of the drivers may not have been compiled in.  This option is called **SoundDriver** in the configuration file.

- [-m](https://www.mankier.com/1/mocp#-m),  [--music-dir](https://www.mankier.com/1/mocp#--music-dir)

  Start in **MusicDir** (set in the configuration file).  This can be also set in the configuration file as **StartInMusicDir**.

- [-q](https://www.mankier.com/1/mocp#-q),  [--enqueue](https://www.mankier.com/1/mocp#--enqueue)

  Add files given after command line options to the queue.  Don't start the interface.

- [-a](https://www.mankier.com/1/mocp#-a),  [--append](https://www.mankier.com/1/mocp#--append)

  Append files, directories (recursively) and playlists given after command line options to the playlist.  Don't start the interface.

- [-c](https://www.mankier.com/1/mocp#-c),  [--clear](https://www.mankier.com/1/mocp#--clear)

  Clear the playlist.

- [-p](https://www.mankier.com/1/mocp#-p),  [--play](https://www.mankier.com/1/mocp#--play)

  Start playing from the first item on the playlist.

- [-l](https://www.mankier.com/1/mocp#-l),  [--playit](https://www.mankier.com/1/mocp#--playit)

  Play files given on the command line without modifying the clients' playlists.

- [-f](https://www.mankier.com/1/mocp#-f),  [--next](https://www.mankier.com/1/mocp#--next)

  Request playing the next song from the server's playlist.

- [-r](https://www.mankier.com/1/mocp#-r),  [--previous](https://www.mankier.com/1/mocp#--previous)

  Request playing the previous song from the server's playlist.

- [-s](https://www.mankier.com/1/mocp#-s),  [--stop](https://www.mankier.com/1/mocp#--stop)

  Request the server to stop playing.

- [-x](https://www.mankier.com/1/mocp#-x),  [--exit](https://www.mankier.com/1/mocp#--exit)

  Bring down the server.

- [-P](https://www.mankier.com/1/mocp#-P),  [--pause](https://www.mankier.com/1/mocp#--pause)

  Request the server to pause playing.

- [-U](https://www.mankier.com/1/mocp#-U),  [--unpause](https://www.mankier.com/1/mocp#--unpause)

  Request the server to resume playing when paused.

- [-G](https://www.mankier.com/1/mocp#-G),  [--toggle-pause](https://www.mankier.com/1/mocp#--toggle-pause)

  Toggle between play and pause.

- [-k](https://www.mankier.com/1/mocp#-k) [**+**|**-**]*N*, [--seek](https://www.mankier.com/1/mocp#--seek) [**+**|**-**]*N*

  Seek forward (positive) or backward (negative) by *N* seconds in the file currently being played.

- [-T](https://www.mankier.com/1/mocp#-T) *THEME*, [--theme](https://www.mankier.com/1/mocp#--theme) *THEME*

  Use a theme file.  If the path is not absolute, the file will be searched for in **/usr/share/moc/themes/** (depends on installation prefix), **~/.moc/themes/** and the current directory.

- [-C](https://www.mankier.com/1/mocp#-C) *FILE*, [--config](https://www.mankier.com/1/mocp#--config) *FILE*

  Use the specified configuration file (which must be readable) instead of  the default.  As this file can specify commands which invoke other  applications MOC will refuse to start if it is not owned by either root  or the current user, or if it is writable by anyone other than its  owner.

- [--no-config](https://www.mankier.com/1/mocp#--no-config)

  Do not read any configuration file but use the built-in defaults.

- [-O](https://www.mankier.com/1/mocp#-O) *NAME*[**+**]**=***VALUE*, [--set-option](https://www.mankier.com/1/mocp#--set-option) *NAME*[**+**]**=***VALUE*

  Override configuration file option NAME with VALUE.  This option can be repeated as many times as needed and the option name is not case sensitive. Most option values are set before the configuration file is processed (which allows the new values to be picked up by substitutions); however,  list-valued options are overridden afterwards (which gives the choice of whether the configured values are replaced or added to).See the example configuration file (**config.example**) for a description of the options available.`Examples: **[-O](https://www.mankier.com/1/mocp#-O) AutoNext=no          [-O](https://www.mankier.com/1/mocp#-O) messagelingertime=1 [-O](https://www.mankier.com/1/mocp#-O) XTerms+=xxt:xwt**`Note that MOC does not perform variable substitution as it does for values read from the configuration file.

- [-M](https://www.mankier.com/1/mocp#-M) *DIR*, [--moc-dir](https://www.mankier.com/1/mocp#--moc-dir) *DIR*

  Use the specified MOC directory instead of the default.  This also causes  the configuration file from that directory to be used.  This can also be specified in the configuration file using the **MOCDir** option.

- [-y](https://www.mankier.com/1/mocp#-y),  [--sync](https://www.mankier.com/1/mocp#--sync)

  This copy of the interface will synchronize its playlist with other clients. This option is called **SyncPlaylist** in the configuration file.

- [-n](https://www.mankier.com/1/mocp#-n),  [--nosync](https://www.mankier.com/1/mocp#--nosync)

  This copy of the interface will not synchronize its playlist with other clients (see above).

- [-A](https://www.mankier.com/1/mocp#-A),  [--ascii](https://www.mankier.com/1/mocp#--ascii)

  Use ASCII characters to draw lines.  (This helps on some terminals.)

- [-i](https://www.mankier.com/1/mocp#-i),  [--info](https://www.mankier.com/1/mocp#--info)

  Print the information about the file currently being played.

- [-Q](https://www.mankier.com/1/mocp#-Q) *FORMAT_STRING*, [--format](https://www.mankier.com/1/mocp#--format) *FORMAT_STRING*

  Print information about the file currently being played using a format  string.  Replace string sequences with the actual information:`**%state**     State **%file**      File **%title**     Title **%artist**    Artist **%song**      SongTitle **%album**     Album **%tt**        TotalTime **%tl**        TimeLeft **%ts**        TotalSec **%ct**        CurrentTime **%cs**        CurrentSec **%b**         Bitrate **%r**         Rate`It is also possible to use variables from the **FormatString** configuration file option.

- [-e](https://www.mankier.com/1/mocp#-e),  [--recursively](https://www.mankier.com/1/mocp#--recursively)

  Alias of **[-a](https://www.mankier.com/1/mocp#-a)** for backward compatibility.

- [-h](https://www.mankier.com/1/mocp#-h),  [--help](https://www.mankier.com/1/mocp#--help)

  Print a list of options with short descriptions and exit.

- [--usage](https://www.mankier.com/1/mocp#--usage)

  Print a synopsis of the mocp command and exit.

- [-V](https://www.mankier.com/1/mocp#-V),  [--version](https://www.mankier.com/1/mocp#--version)

  Print the program version and exit.

- [--echo-args](https://www.mankier.com/1/mocp#--echo-args)

  Print the POPT-interpreted command line arguments and exit.

- [-v](https://www.mankier.com/1/mocp#-v) [**+**|**-**]*N*, [--volume](https://www.mankier.com/1/mocp#--volume) [**+**|**-**]*N*

  Adjust the mixer volume.  You can set (**[-v](https://www.mankier.com/1/mocp#-v) 50**) or adjust (**[-v](https://www.mankier.com/1/mocp#-v) +10**, **[-v](https://www.mankier.com/1/mocp#-v) -10**).

- [-t](https://www.mankier.com/1/mocp#-t) *OPTION*[**,**...], [--toggle](https://www.mankier.com/1/mocp#--toggle) *OPTION*[**,**...]

- [-o](https://www.mankier.com/1/mocp#-o) *OPTION*[**,**...], [--on](https://www.mankier.com/1/mocp#--on) *OPTION*[**,**...]

- [-u](https://www.mankier.com/1/mocp#-u) *OPTION*[**,**...], [--off](https://www.mankier.com/1/mocp#--off) *OPTION*[**,**...]

  Followed by a list of identifiers, these will control MOC's playlist options.  Valid identifiers are **shuffle**, **repeat** and **autonext**. They can be shortened to '**s**', '**r**' and '**n**' respectively. Both the identifiers and short forms are case insensitive.`Example: **[-t](https://www.mankier.com/1/mocp#-t) shuffle,R,n**`    would toggle shuffle, repeat and autonext all at once.

- [-j](https://www.mankier.com/1/mocp#-j) *N*{**s**|**%**}, [--jump](https://www.mankier.com/1/mocp#--jump) *N*{**s**|**%**}

  Jump to some position in the current file.  *N* is the number of seconds (when followed by an '**s**') or the percent of total file time (when followed by a '**%**').`Examples: **[-j](https://www.mankier.com/1/mocp#-j) 10s**, **[-j](https://www.mankier.com/1/mocp#-j) 50%**`

Using Popt Aliases

MOC uses the POPT library to process its command line.  This allows users  to assign MOC options and arguments to an alias of their choosing. The  aliases are just lines in the **~/.popt** text file and have the general form:

```
mocp alias newoption expansion
```

This works as if *expansion* textually replaces *newoption* on the command line.  The replacement is recursive; that is, other *newoption*s can be embedded in the *expansion*. The *expansion* is parsed similarly to a shell command, which allows \, ", and ' to be  used for quoting.  If a backslash is the final character on a line, the  next line in the file is assumed to be a logical continuation of the  line containing the backslash, just as in the shell.  The *newoption* can be either a short or long option, and any syntactically valid name the user wishes to use.

If you add a description for the new option and/or for any argument by appending the special POPT options **--POPTdesc** and **--POPTargs**, then the option will be displayed in the output of **[--help](https://www.mankier.com/1/mocp#--help)** and **[--usage](https://www.mankier.com/1/mocp#--usage)**.  The value for these two options are strings of the form **$"***string***"**.

So, for example:

```
mocp alias --single -D --set-option autonext=no \
           --POPTdesc=$"Play just the file selected"
```

would allow the user to turn on logging (**[-D](https://www.mankier.com/1/mocp#-D)**) and override the configuration file's **AutoNext** option setting just by using **--single** as an option to the mocp command.

Sometimes you may wish to provide values to aliased options from the command  line.  If just one aliased option has such a value, then it's a simple  matter of placing it last:

```
mocp alias --yours --sound-driver OSS --theme
```

when used like this:

```
mocp --yours your_theme
```

would result in:

```
mocp --sound-driver OSS --theme your_theme
```

But aliasing multiple options with such values means making use of the special construct **!#:+** (and quoting carefully):

```
mocp alias -1 "-R !#:+" "-T my_theme" "-O !#:+"
```

when used like this:

```
mocp -1 OSS shuffle=yes ~/my_music
```

would result in:

```
mocp -R OSS -T my_theme -O shuffle=yes ~/my_music
```

There is also a **~/.popt** entry which allows for the execution of a different program when the associated option is used.  For this, an **exec** is used in place of the **alias** and the *expansion* is the program to be executed:

```
mocp exec --help /usr/bin/man 1 mocp \
           POPTdesc=$"Provide the man page instead of help"
```

This would override the usual MOC **[--help](https://www.mankier.com/1/mocp#--help)** output and use the system's **man** program to present this man page instead.

Note that while **~/.popt** (or **/etc/popt**) is the default POPT configuration file, you can nominate specific file(s) to be used instead via the **MOCP_POPTRC** environment variable.

Environment Variables

The following environment variables are used directly by MOC.  Additional  variables may be relevant to the libraries MOC uses.  Also, any  environment environment variable may be substituted into a configuration file option value (see the 'config.example' file for details).

- [**ESCDELAY**](https://www.mankier.com/1/mocp#Environment_Variables-ESCDELAY)

  An ncurses(3X) variable which specifies the delay (in milliseconds) after  which it will treat an ESC as a standalone key and not part of an  escaped character sequence (such as is generated by function keys). MOC  sets this value to 25ms by default, which is sufficient for most  systems.

- [**HOME**](https://www.mankier.com/1/mocp#Environment_Variables-HOME)

  Tells MOC where your home directory is located and is used for various  purposes, including the default location of the MOC directory.

- [**MOCP_OPTS**](https://www.mankier.com/1/mocp#Environment_Variables-MOCP_OPTS)

  The value of this variable will be prepended to the command line options before they are processed.

- [**MOCP_POPTRC**](https://www.mankier.com/1/mocp#Environment_Variables-MOCP_POPTRC)

  A colon-separated list of POPT configuration files which will be loaded  in sequence by MOC during initialisation.  If the variable is unset then the default POPT configuration file will be used.  If the variable is  set but empty then no POPT configuration file will be loaded.  If the  variable is set then those files which exist will be loaded and those  which don't will be skipped.As these files can specify commands  which invoke other applications, MOC will refuse to start if they are  not owned by root or the current user, or they are writable by anyone  other than their owner.

- [**TERM**](https://www.mankier.com/1/mocp#Environment_Variables-TERM) and [**WINDOW**](https://www.mankier.com/1/mocp#Environment_Variables-WINDOW)

  Used by MOC to distinguish between X-terminals, [screen(1)](https://www.mankier.com/1/screen) and console terminals.  MOC uses the configuration file options **XTerms** and **ScreenTerms** to help make this determination.

Files

- [**~/.moc**](https://www.mankier.com/1/mocp#Files-~/.moc)

  MOC directory for the configuration file, socket, the pid file and other data.

- [**~/.moc/config**](https://www.mankier.com/1/mocp#Files-~/.moc/config)

  Configuration file for MOC.  The format is very simple; to see how to use it look at the example configuration file (**config.example**) distributed with the program.  The example file fully describes all the configuration options, and so is a useful reference when using the **[-O](https://www.mankier.com/1/mocp#-O)** option.  As this file can specify commands which invoke other  applications MOC will refuse to start if it is not owned by either root  or the current user, or if it is writable by anyone other than its  owner.

- [**~/.popt**](https://www.mankier.com/1/mocp#Files-~/.popt)

- [**/etc/popt**](https://www.mankier.com/1/mocp#Files-/etc/popt)

  The default files POPT reads to obtain aliased options.  As these files can specify commands which invoke other applications, MOC will refuse to  start if it is not owned by root or the current user, or if it is  writable by anyone other than its owner.  (Also see the **MOCP_POPTRC** environment variable above.)

- [**~/.moc/themes**](https://www.mankier.com/1/mocp#Files-~/.moc/themes)

- [**/usr/share/moc/themes**](https://www.mankier.com/1/mocp#Files-/usr/share/moc/themes)

  Default directories for the theme files.

- [**/usr/share/moc/decoder_plugins**](https://www.mankier.com/1/mocp#Files-/usr/share/moc/decoder_plugins)

  Default directories for the audio decoder plugins.

- [**mocp_client_log**](https://www.mankier.com/1/mocp#Files-mocp_client_log)

- [**mocp_server_log**](https://www.mankier.com/1/mocp#Files-mocp_server_log)

  Client and server log files.  These files are created in the directory in  which the client and server are started.  (Also see the **[-D](https://www.mankier.com/1/mocp#-D)** option.)

Bugs

Command line options that affect the server behaviour (like **[--sound-driver](https://www.mankier.com/1/mocp#--sound-driver)**) are ignored if the server is already running at the time of executing **mocp**.  The user is not warned about this.

Homepage

http://moc.daper.net/

Author

Damian Pietras   <daper@daper.net>
MOC Maintainer(s)  <mocmaint@daper.net>

Info

16 November 2016 Version 2.6-alpha3 Music On Console
