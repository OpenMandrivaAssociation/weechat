%define name weechat
%define version 0.2.5
%define release %mkrel 1

%define weegtk 0
%define weeqt 0

%{?_without_gtk: %{expand: %%define weegkt 0}}
%{?_with_gtk: %{expand: %%define weegkt 1}}
%{?_without_qt: %{expand: %%define weeqt 0}}
%{?_with_qt: %{expand: %%define weeqt 1}}

Summary: Wee Enhanced Environment for Chat
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://weechat.flashtux.org/download/%{name}-%{version}.tar.bz2
# Mandriva nicely use -D_FORTIFY_SOURCE=2 wich cause in stdio a #define printf
# there is no simple way to disable this in optflags
# this patch rename printf to printf_client to avoid the issue
Patch1: weechat_docbookpath.patch
License: GPL
Group: Networking/IRC
Url: http://weechat.flashtux.org/
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: ncurses-devel
BuildRequires: perl-devel
# Ruby & Python are really needed for the build, tks lbd
BuildRequires: python-devel
BuildRequires: ruby-devel
Buildrequires: lua-devel
BuildRequires: aspell-devel

%if %weegtk
BuildRequires: libgtk+2-devel
%endif
%if %weeqt
BuildRequires: qt3-devel
%endif

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

Install %name-gtk to have the gtk-gui.

%if %weegtk
%package gtk
Group: Networking/IRC
Summary: Wee Enhanced Environment for Chat (With GTK)
Requires: %name = %version

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

This package contain %name-gtk

%endif

%if %weeqt
%package qt
Group: Networking/IRC
Summary: Wee Enhanced Environment for Chat (With GTK)
Requires: %name = %version

%description qt
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

This package contain %name-qt

%endif

%package perl
Group: Networking/IRC
Summary: Weechat perl plugins
Requires: %name = %version

%description perl
This package allow weechat to use perl scripts


%package python
Group: Networking/IRC
Summary: Weechat python plugins
Requires: %name = %version

%description python
This package allow weechat to use python scripts

%package ruby
Group: Networking/IRC
Summary: Weechat ruby plugins
Requires: %name = %version

%description ruby
This package allow weechat to use ruby scripts

%package lua
Group: Networking/IRC
Summary: Weechat lua plugins
Requires: %name = %version

%description lua
This package allow weechat to use lua scripts

%package charset
Group: Networking/IRC
Summary: Weechat charset plugins
Requires: %name = %version

%description charset
This package allow weechat to use charset

%package aspell
Group: Networking/IRC
Summary: Weechat aspell plugins
Requires: %name = %version

%description aspell
This package allow weechat to use aspell

%prep
%setup -q
#%patch1 -p1

%build
%configure  --with-doc-xsl-prefix=%_datadir/sgml/docbook/xsl-stylesheets/ \
%if %weegtk
    --enable-gtk \
%endif
%if %weeqt
    --enable-qt \
%endif
    --enable-perl \
    --enable-python \
    --enable-ruby

%make

%install
%makeinstall_std

(
cd %buildroot%_bindir
ln -s %name-curses %name
)

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info


%files -f %name.lang
%defattr(-,root,root)
%_bindir/%name
%_bindir/%name-curses
%_mandir/man1/weechat*
%dir %_prefix/lib*/%name
%dir %_prefix/lib*/%name/plugins
%doc FAQ.fr FAQ README NEWS ChangeLog AUTHORS BUGS TODO

%files perl
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*perl*

%files python
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*python*

%files ruby
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*ruby*

%files lua
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*lua*

%files aspell
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*aspell*

%files charset
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*charset*

%if %weegtk
%files gtk
%defattr(-,root,root)
%_bindir/%name-gtk
%doc FAQ.fr FAQ README NEWS ChangeLog AUTHORS BUGS TODO
%endif

%if %weeqt
%files qt
%defattr(-,root,root)
%_bindir/%name-qt
%doc FAQ.fr FAQ README NEWS ChangeLog AUTHORS BUGS TODO
%endif
