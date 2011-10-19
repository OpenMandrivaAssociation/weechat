%define	Werror_cflags %nil
%define	weegtk 1

%{?_without_gtk: %{expand: %%define	weegtk 0}}
%{?_with_gtk: %{expand: %%define	weegtk 1}}

Name:		weechat
Version:	0.3.5
Release:	1
Summary:	Wee Enhanced Environment for Chat
Source0:	http://www.weechat.org/files/src/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Networking/IRC
URL:		http://www.weechat.org/

BuildRequires:	cmake
BuildRequires:	ncurses-devel
# next need for utf8 support
BuildRequires:	ncursesw-devel
BuildRequires:	perl-devel
# Ruby & Python are really needed for the build, tks lbd
BuildRequires:	python-devel
BuildRequires:	ruby-devel
BuildRequires:	lua-devel
BuildRequires:	aspell-devel
BuildRequires:	gettext-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	tcl-devel

%description
WeeChat (Wee Enhanced Environment for Chat) is a free IRC client, fast and
light, designed for many operating systems.

Main features are:
  - multi-servers connection
  - many GUI (Graphical User Interface): Curses, Gtk and Qt
  - small, fast and light
  - customizable and extensible with scripts
  - compliant with RFCs 1459, 2810, 2811, 2812, and 2813
  - multi-platform (Gnu/Linux, *BSD, Windows and other)
  - 100% GPL, free software

Install %{name}-gtk to have the gtk-gui.

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}-curses
%{_libdir}/alias.so*
%{_libdir}/fifo.so*
%{_libdir}/irc.so*
%{_libdir}/logger.so*
%{_libdir}/xfer.so*

#--------------------------------------------------------------------

%if %weegtk
%package gtk
Group:		Networking/IRC
Summary:	Wee Enhanced Environment for Chat (With GTK)
Requires:	%{name} = %{version}

%description gtk
WeeChat (Wee Enhanced Environment for Chat) is a free IRC client, fast and
light, designed for many operating systems.

Main features are:
  - multi-servers connection
  - many GUI (Graphical User Interface): Curses, Gtk and Qt
  - small, fast and light
  - customizable and extensible with scripts
  - compliant with RFCs 1459, 2810, 2811, 2812, and 2813
  - multi-platform (Gnu/Linux, *BSD, Windows and other)
  - 100% GPL, free software

This package contain %{name}-gtk

%files gtk
%defattr(-,root,root)
%{_bindir}/%{name}-gtk
%endif

#--------------------------------------------------------------------

%package perl
Group:		Networking/IRC
Summary:	Weechat perl plugins
Requires:	%{name} = %{version}

%description perl
This package allow weechat to use perl scripts

%files perl
%defattr(-,root,root)
%{_libdir}/perl.so*

#--------------------------------------------------------------------

%package python
Group:		Networking/IRC
Summary:	Weechat python plugins
Requires:	%{name} = %{version}

%description python
This package allow weechat to use python scripts

%files python
%defattr(-,root,root)
%{_libdir}/python.so*

#--------------------------------------------------------------------

%package tcl
Group:		Networking/IRC
Summary:	Weechat tcl plugins
Requires:	%{name} = %{version}

%description tcl
This package allow weechat to use tcl scripts

%files tcl
%defattr(-,root,root)
%{_libdir}/tcl.so*

#--------------------------------------------------------------------

%package ruby
Group:		Networking/IRC
Summary:	Weechat ruby plugins
Requires:	%{name} = %{version}

%description ruby
This package allow weechat to use ruby scripts

%files ruby
%defattr(-,root,root)
%{_libdir}/ruby.so*

#--------------------------------------------------------------------

%package lua
Group:		Networking/IRC
Summary:	Weechat lua plugins
Requires:	%{name} = %{version}

%description lua
This package allow weechat to use lua scripts

%files lua
%defattr(-,root,root)
%{_libdir}/lua.so*

#--------------------------------------------------------------------

%package charset
Group:		Networking/IRC
Summary:	Weechat charset plugins
Requires:	%{name} = %{version}

%description charset
This package allow weechat to use charset

%files charset
%defattr(-,root,root)
%{_libdir}/charset.so*

#--------------------------------------------------------------------

%package aspell
Group:		Networking/IRC
Summary:	Weechat aspell plugins
Requires:	%{name} = %{version}

%description aspell
This package allow weechat to use aspell

%files aspell
%defattr(-,root,root)
%{_libdir}/aspell.so*

#--------------------------------------------------------------------

%package relay
Group:		Networking/IRC
Summary:	Weechat IRC proxy plugin
Requires:	%{name} = %{version}

%description relay
This package allows weechat to use an IRC proxy

%files relay
%defattr(-,root,root)
%{_libdir}/relay.so*

#--------------------------------------------------------------------

%package rmodifier
Group:		Networking/IRC
Summary:	Weechat IRC regex modifier plugin
Requires:	%{name} = %{version}

%description rmodifier
alter modifier strings with regular expression

%files rmodifier
%defattr(-,root,root)
%{_libdir}/rmodifier.so*

#--------------------------------------------------------------------

%package  devel
Summary:	Development files for weechat
Group:		Development/C
Requires:	%{name} = %{version}-%{release} pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.

%files devel
%defattr(-,root,root)
%{_includedir}/weechat
%{_libdir}/pkgconfig/weechat.pc
%{_libdir}/*a

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x	\
%if %{weegtk}
		--enable-gtk \
%else
		--disable-gtk \
%endif

%cmake

%install
%makeinstall

(
cd %{buildroot}%{_bindir}
ln -s %{name}-curses %{name}
)

%find_lang %{name}

%clean
rm -rf %{buildroot}

