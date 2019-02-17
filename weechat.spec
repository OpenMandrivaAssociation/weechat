Summary:	Portable, fast, light and extensible IRC client
Name:		weechat
Version:	2.4
Release:	1
Source0:	http://www.weechat.org/files/src/%{name}-%{version}.tar.bz2
#Patch0:		weechat-combined.patch
License:	GPLv3
Group: 		Networking/IRC
Url: 		http://www.weechat.org/
BuildRequires:  aspell-devel
BuildRequires: 	cmake
BuildRequires: 	pkgconfig(ncurses)
BuildRequires:	pkgconfig(libcurl)
# need for utf8 support
BuildRequires: 	ncursesw-devel
BuildRequires: 	perl-devel
BuildRequires:  perl-ExtUtils-Embed
BuildRequires:  php-devel
# Ruby & Python are really needed for the build, tks lbd
# Python2 is needed but use Python3 is possible but "NOT recommended because many \"official\" scripts won't work"
# So stay for now with Python2 (penguin).
BuildRequires: 	pkgconfig(python2)
BuildRequires: 	ruby-devel
Buildrequires: 	pkgconfig(lua)
BuildRequires: 	enchant-devel
BuildRequires: 	gettext
BuildRequires:	docbook-style-xsl
BuildRequires: 	pkgconfig(gnutls)
BuildRequires:	libgcrypt-devel
BuildRequires: 	tcl-devel

Obsoletes:	%{name}-gtk

%description
WeeChat (Wee Enhanced Environment for Chat) is a fast, light and extensible
chat client designed for many platforms.
 
Main features are: 
- modular: a lightweight core with plugins around
- multi-protocols: IRC and Jabber (other soon)
- extensible: C plugins and scripts (Perl, Python, Ruby, Lua and Tcl)
- free software: released under GPLv3 license
- fully documented: user's guide, API, FAQ,.. translated in many languages 



%files -f %name.lang
#doc *.html
%_bindir/%name
%_bindir/%name-curses
%{_bindir}/%{name}-headless
#_mandir/man1/weechat*
%dir %_libdir/%{name}
%dir %_libdir/%{name}/plugins
%{_libdir}/%name/plugins/alias.so
%{_libdir}/%{name}/plugins/buflist.so
%{_libdir}/%{name}/plugins/exec.so
%{_libdir}/%{name}/plugins/fset.so
%{_libdir}/%name/plugins/fifo.so
%{_libdir}/%name/plugins/irc.so
%{_libdir}/%name/plugins/logger.so
%{_libdir}/%name/plugins/relay.so
#{_libdir}/%name/plugins/rmodifier.so
%{_libdir}/%name/plugins/xfer.so
%{_libdir}/%name/plugins/script.so
%{_libdir}/%{name}/plugins/trigger.so
%{_iconsdir}/hicolor/32x32/apps/%{name}.png

#--------------------------------------------------------------------

%package perl
Group:		Networking/IRC
Summary: 	Weechat perl plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description perl
This package allow weechat to use perl scripts

%files perl
%{_libdir}/%name/plugins/perl.so

#--------------------------------------------------------------------

%package python
Group:		Networking/IRC
Summary:	Weechat python plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description python
This package allow weechat to use python scripts

%files python
%{_libdir}/%name/plugins/python.so

#--------------------------------------------------------------------

%package tcl
Group:		Networking/IRC
Summary:	Weechat tcl plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description tcl
This package allow weechat to use tcl scripts

%files tcl
%{_libdir}/%name/plugins/tcl.so

#--------------------------------------------------------------------

%package ruby
Group:		Networking/IRC
Summary:	Weechat ruby plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description ruby
This package allow weechat to use ruby scripts

%files ruby
%{_libdir}/%name/plugins/ruby.so

#--------------------------------------------------------------------

%package lua
Group:		Networking/IRC
Summary:	Weechat lua plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description lua
This package allow weechat to use lua scripts

%files lua
%{_libdir}/%name/plugins/lua.so

#--------------------------------------------------------------------

%package charset
Group:		Networking/IRC
Summary:	Weechat charset plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description charset
This package allow weechat to use charset

%files charset
%{_libdir}/%name/plugins/charset.so

#--------------------------------------------------------------------
%if 1
%package aspell
Group:		Networking/IRC
Summary:	Weechat spell check plugins
Requires:	%name = %version
Conflicts:	%name < 0.3.6

%description aspell
This package allow weechat to use spell checker feature.

%files aspell
%{_libdir}/%name/plugins/aspell.so
%endif

#--------------------------------------------------------------------

%package  devel
Summary:	Development files for weechat
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

#--------------------------------------------------------------------

%prep
%setup -q
#patch0 -p1

%build
%cmake -DLIBDIR=%{_libdir}
%make_build

%install
%make_install -C build

#(
#cd %buildroot%_bindir
#ln -s %name-curses %name
#)

%find_lang %name
