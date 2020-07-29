// C-Obfuscator sample output, Obfuscated tic-tac-toe game

#include <ncurses.h>
#include <time.h>
#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
void srpc ( char * fdvp ) ; char ogsp ( char * fdvp , uint8_t btxz ) ; uint8_t owsb ( char * fdvp
, char * * twtv ) ; void aboq ( char * fdvp , char buji , uint8_t btxz ) ; void mkkr ( char * fdvp
, char buji ) ; void rusy ( char * fdvp , char buji , uint8_t btcm ) ; uint8_t kcdb ( const char
* fdvp ) ; void srpc ( char * fdvp ) { srand ( time ( NULL ) ) ; for ( char * ruxi = fdvp ; ruxi < fdvp
+ 0x9 ; ++ ruxi ) * ruxi = 0x20 ; } char ogsp ( char * fdvp , uint8_t btxz ) { assert ( 0x0 <= btxz
&& btxz <= 0x8 ) ; return fdvp [ btxz ] ; } uint8_t owsb ( char * fdvp , char * * twtv ) { char * *
sqwx = twtv ; for ( char * bkil = fdvp ; bkil < fdvp + 0x9 ; ++ bkil ) { if ( * bkil == 0x20 ) * sqwx
++ = bkil ; } return sqwx - twtv ; } void aboq ( char * fdvp , char buji , uint8_t btxz ) { assert
( 0x0 <= btxz && btxz <= 0x8 ) ; fdvp [ btxz ] = buji ; } void mkkr ( char * fdvp , char buji ) { char
* uzkx [ 0x9 ] ; uint8_t pwzq = owsb ( fdvp , uzkx ) ; * uzkx [ rand ( ) % pwzq ] = buji ; } static void
ywjp ( const char * fdvp , uint16_t * dqyg ) { dqyg [ 0x0 ] = fdvp [ 0x0 ] + fdvp [ 0x1 ] + fdvp [ 0x2
] ; dqyg [ 0x1 ] = fdvp [ 0x3 ] + fdvp [ 0x4 ] + fdvp [ 0x5 ] ; dqyg [ 0x2 ] = fdvp [ 0x6 ] + fdvp [ 0x7 ]
+ fdvp [ 0x8 ] ; dqyg [ 0x3 ] = fdvp [ 0x0 ] + fdvp [ 0x3 ] + fdvp [ 0x6 ] ; dqyg [ 0x4 ] = fdvp [ 0x1 ] +
fdvp [ 0x4 ] + fdvp [ 0x7 ] ; dqyg [ 0x5 ] = fdvp [ 0x2 ] + fdvp [ 0x5 ] + fdvp [ 0x8 ] ; dqyg [ 0x7 ] = fdvp
[ 0x6 ] + fdvp [ 0x4 ] + fdvp [ 0x2 ] ; dqyg [ 0x6 ] = fdvp [ 0x0 ] + fdvp [ 0x4 ] + fdvp [ 0x8 ] ; } void
rusy ( char * fdvp , char buji , uint8_t btcm ) { char * eaev = fdvp ; char * uzkx [ 0x9 ] ; owsb
( fdvp , uzkx ) ; uint8_t wogy [ 0x9 ] ; wogy [ 0x0 ] = 0x1 | 0x8 | 0x40 ; wogy [ 0x1 ] = 0x1 | 0x10 ;
wogy [ 0x2 ] = 0x1 | 0x20 | 0x80 ; wogy [ 0x3 ] = 0x2 | 0x8 ; wogy [ 0x4 ] = 0x2 | 0x10 | 0x80 | 0x40 ;
wogy [ 0x5 ] = 0x2 | 0x20 ; wogy [ 0x6 ] = 0x4 | 0x8 | 0x80 ; wogy [ 0x7 ] = 0x4 | 0x10 ; wogy [ 0x8 ] =
0x4 | 0x20 | 0x40 ; uint16_t dqyg [ 0x8 ] ; ywjp ( fdvp , dqyg ) ; uint8_t kcsg = 0x0 ; for ( uint8_t
gccx = 0x0 ; gccx < 0x9 ; ++ gccx ) { uint8_t dhid = 0x0 ; if ( fdvp [ gccx ] != 0x20 ) continue ;
uint8_t btxz = 0x0 ; for ( uint8_t wvva = 0x1 ; wvva ; wvva <<= 0x1 ) { if ( wogy [ gccx ] & wvva
) { if ( dqyg [ btxz ] == 0x2 * 0x4f + 0x20 ) dhid += 0x32 ; if ( dqyg [ btxz ] == 0x2 * 0x58 + 0x20 )
dhid += 0x14 ; if ( dqyg [ btxz ] == 0x4f + 0x2 * 0x20 ) dhid += 0x3 ; if ( dqyg [ btxz ] == 0x58 + 0x2
* 0x20 ) dhid += 0x2 ; if ( dqyg [ btxz ] == 0x3 * 0x20 ) dhid += 0x1 ; } ++ btxz ; } if ( dhid > kcsg
|| ( dhid == kcsg && rand ( ) % 0x2 ) ) { kcsg = dhid ; eaev = fdvp + gccx ; } } if ( fdvp [ 0x0 ] == fdvp
[ 0x8 ] && fdvp [ 0x2 ] == fdvp [ 0x6 ] && btcm == 0x2 && ( fdvp [ 0x2 ] == 0x58 || fdvp [ 0x0 ] == 0x58
) ) fdvp [ 0x2 * ( rand ( ) % 0x4 ) + 0x1 ] = 0x4f ; else * eaev = 0x4f ; } uint8_t kcdb ( const char
* fdvp ) { uint8_t stje = 0x0 ; uint16_t dqyg [ 0x8 ] ; ywjp ( fdvp , dqyg ) ; for ( const uint16_t
* ruxi = dqyg ; ruxi < dqyg + 0x8 ; ++ ruxi ) { if ( * ruxi == 0x3 * 0x58 ) return 0x1 ; if ( * ruxi ==
0x3 * 0x4f ) return 0x2 ; if ( * ruxi > 0x3 * 0x4f ) ++ stje ; } if ( stje == 0x8 ) return 0x3 ; return
0x0 ; } uint8_t aofn ( uint8_t yjwc ) ; uint8_t nxoq ( ) ; int8_t xgoh ( char * fdvp , char buji
) ; void cyjm ( const char * fdvp ) ; void hush ( int8_t lwbj , int8_t dzok ) ; void fftq ( ) ; int
main ( ) { initscr ( ) ; noecho ( ) ; int8_t lwbj = - 0x1 ; while ( true ) { fftq ( ) ; int8_t dzok
= 0x0 ; while ( ( dzok != 0x71 && dzok > 0x33 ) || dzok < 0x31 ) dzok = wgetch ( stdscr ) ; if ( dzok
== 0x31 ) lwbj = aofn ( 0x1 ) ; else if ( dzok == 0x32 ) lwbj = aofn ( 0x0 ) ; else if ( dzok == 0x33
) lwbj = nxoq ( ) ; if ( dzok == 0x71 ) break ; if ( lwbj == 0x0 ) continue ; hush ( lwbj , dzok ) ;
int jxlf = - 0x1 ; while ( lwbj != 0x0 && jxlf == - 0x1 ) jxlf = wgetch ( stdscr ) ; } endwin ( ) ;
return EXIT_SUCCESS ; } uint8_t aofn ( uint8_t yjwc ) { uint8_t lwbj = 0x0 ; uint8_t btcm
= 0x1 ; char fdvp [ 0x9 ] ; srpc ( fdvp ) ; cyjm ( fdvp ) ; while ( lwbj == 0x0 ) { if ( xgoh ( fdvp ,
0x58 ) == 0x0 ) return lwbj ; cyjm ( fdvp ) ; lwbj = kcdb ( fdvp ) ; if ( lwbj != 0x0 ) return lwbj
; if ( yjwc == 0x0 ) rusy ( fdvp , 0x4f , btcm ) ; else mkkr ( fdvp , 0x4f ) ; cyjm ( fdvp ) ; lwbj =
kcdb ( fdvp ) ; if ( lwbj != 0x0 ) return lwbj ; ++ btcm ; } return lwbj ; } uint8_t nxoq ( ) { uint8_t
lwbj = 0x0 ; char fdvp [ 0x9 ] ; srpc ( fdvp ) ; cyjm ( fdvp ) ; char buji = 0x58 ; do { if ( xgoh ( fdvp
, buji ) == 0x0 ) return lwbj ; cyjm ( fdvp ) ; lwbj = kcdb ( fdvp ) ; if ( buji == 0x58 ) buji = 0x4f
; else buji = 0x58 ; } while ( lwbj == 0x0 ) ; return lwbj ; } int8_t xgoh ( char * fdvp , char buji
) { int jxlf = 0x0 ; while ( jxlf != 0x71 && ( ( 0x31 > jxlf || jxlf > 0x39 ) || fdvp [ jxlf - 0x31
] != 0x20 ) ) jxlf = wgetch ( stdscr ) ; if ( jxlf == 0x71 ) return 0x0 ; else { aboq ( fdvp , buji
, jxlf - 0x31 ) ; return 0x1 ; } } void mvjf ( const int8_t taio ) { for ( int wvva = 0x0 ; wvva <
LINES / 0x2 - taio / 0x2 ; ++ wvva ) printw ( "\xa" ) ; } void uhgr ( const int8_t eyxo ) { for (
int wvva = 0x0 ; wvva < COLS / 0x2 - eyxo / 0x2 ; ++ wvva ) printw ( "\x20" ) ; } void fftq ( ) { const
int8_t sftp = 0x20 ; const int8_t ciyr = 0xb ; const char * kbfs = "\x20\x20\x20\x20\x20\x57\x65\x6c\x63\x6f\x6d\x65\x20\x74\x6f\x20\x54\x69\x63\x2d\x54\x61\x63\x2d\x54\x6f\x65\x20\x20\x20\x20\x20\xa"
; const char * karq = "\x20\x20\x20\x20\x20\x63\x72\x65\x61\x74\x65\x64\x20\x62\x79\x20\x44\x61\x76\x69\x64\x20\x56\x65\x6c\x6c\x61\x20\x20\x20\x20\x20\xa"
; const char * qjgs = "\x20\x20\x20\x20\x70\x72\x65\x73\x73\x20\x31\x2d\x33\x20\x74\x6f\x20\x73\x65\x6c\x65\x63\x74\x20\x6d\x6f\x64\x65\x20\x20\x20\x20\xa"
; const char * ujqj = "\x20\x20\x31\x20\x2d\x20\x70\x6c\x61\x79\x65\x72\x20\x76\x73\x20\x65\x61\x73\x79\x20\x63\x70\x75\x20\x20\x20\x20\x20\x20\x20\x20\xa"
; const char * tdrz = "\x20\x20\x32\x20\x2d\x20\x70\x6c\x61\x79\x65\x72\x20\x76\x73\x20\x69\x6d\x70\x6f\x73\x73\x69\x62\x6c\x65\x20\x63\x70\x75\x20\x20\xa"
; const char * wdwc = "\x20\x20\x33\x20\x2d\x20\x74\x77\x6f\x20\x70\x6c\x61\x79\x65\x72\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\xa"
; const char * khud = "\x20\x20\x20\x20\x70\x72\x65\x73\x73\x20\x71\x20\x61\x6e\x79\x74\x69\x6d\x65\x20\x74\x6f\x20\x6c\x65\x61\x76\x65\x20\x20\x20\x20\xa"
; werase ( stdscr ) ; mvjf ( ciyr ) ; uhgr ( sftp ) ; printw ( kbfs ) ; uhgr ( sftp ) ; printw ( karq
) ; printw ( "\xa" ) ; uhgr ( sftp ) ; printw ( qjgs ) ; printw ( "\xa" ) ; uhgr ( sftp ) ; printw
( ujqj ) ; uhgr ( sftp ) ; printw ( tdrz ) ; uhgr ( sftp ) ; printw ( wdwc ) ; printw ( "\xa" ) ; uhgr
( sftp ) ; printw ( khud ) ; wrefresh ( stdscr ) ; curs_set ( 0x0 ) ; } void cyjm ( const char *
fdvp ) { const int8_t cbas = 0x24 ; const int8_t yofi = 0x5 ; const char * siqn = "\x20\x20\x20\x20\x20\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x20\x20\x20\x20\x20\x20\x20\x20\x5b\x31\x5d\x5b\x32\x5d\x5b\x33\x5d\x20\x20\x20\x20\x20\xa"
; const char * avyf = "\x20\x20\x20\x20\x20\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x20\x20\x20\x20\x20\x20\x20\x20\x5b\x34\x5d\x5b\x35\x5d\x5b\x36\x5d\x20\x20\x20\x20\x20\xa"
; const char * rhrr = "\x20\x20\x20\x20\x20\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x5b\x25\x63\x5d\x20\x20\x20\x20\x20\x20\x20\x20\x5b\x37\x5d\x5b\x38\x5d\x5b\x39\x5d\x20\x20\x20\x20\x20\xa"
; const char * gvyy = "\x63\x68\x6f\x6f\x73\x65\x20\x61\x20\x73\x70\x61\x63\x65\x20\x62\x79\x20\x70\x72\x65\x73\x73\x69\x6e\x67\x20\x61\x20\x6b\x65\x79\x20\x31\x2d\x39\xa"
; werase ( stdscr ) ; mvjf ( yofi ) ; uhgr ( cbas ) ; printw ( siqn , fdvp [ 0x0 ] , fdvp [ 0x1 ] , fdvp
[ 0x2 ] ) ; uhgr ( cbas ) ; printw ( avyf , fdvp [ 0x3 ] , fdvp [ 0x4 ] , fdvp [ 0x5 ] ) ; uhgr ( cbas )
; printw ( rhrr , fdvp [ 0x6 ] , fdvp [ 0x7 ] , fdvp [ 0x8 ] ) ; printw ( "\xa" ) ; uhgr ( cbas ) ; printw
( gvyy ) ; wrefresh ( stdscr ) ; curs_set ( 0x0 ) ; } void hush ( int8_t lwbj , int8_t dzok ) {
printw ( "\xa" ) ; if ( lwbj == 0x1 ) { if ( dzok == 0x31 || dzok == 0x32 ) { uhgr ( 0xc ) ; printw
( "\x50\x6c\x61\x79\x65\x72\x20\x57\x69\x6e\x73\x21" ) ; } else { uhgr ( 0xe ) ; printw
( "\x50\x6c\x61\x79\x65\x72\x20\x31\x20\x57\x69\x6e\x73\x21" ) ; } } else if ( lwbj
== 0x2 ) { if ( dzok == 0x31 || dzok == 0x32 ) { uhgr ( 0x8 ) ; printw ( "\x43\x50\x55\x20\x57\x69\x6e\x73"
) ; } else { uhgr ( 0xe ) ; printw ( "\x50\x6c\x61\x79\x65\x72\x20\x32\x20\x57\x69\x6e\x73\x21"
) ; } } else { uhgr ( 0xc ) ; printw ( "\x49\x74\x27\x73\x20\x61\x20\x54\x69\x65" ) ; }
curs_set ( 0x0 ) ; }
