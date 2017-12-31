

##BEGIN START-UP SEQUENCE
##()->(n,j,k,t0)

#n                          (n),←
#n,n                        (n,j),Đ
#n,n,0                      (n,j,k),0
#n,n,0,0                    (n,j,k,t0),0
#n,n,0,0,0                  (n,j,k,t0,0),0

##END START-UP SEQUENCE


##BEGIN INNER LOOP

##BEGIN BUILDING STACK NEEDED FOR CALCULATIONS
##(n,j,k,t0)->(n,j,k,t0,j,k,n,j,k,k)

#n,n,0,0,0                  (n,j,k,t0,0),`
#n,n,0,0                    (n,j,k,t0),ŕ
#n,n,0,0,4                  (n,j,k,t0,4),4
#0,0,n,n                    (t0,k,j,n),Ș
#0,0,n,n,n                  (t0,k,j,n,n),Đ
#0,0,n,n,n,4                (t0,k,j,n,n,4),4
#0,n,n,n,0                  (t0,n,n,j,k),Ș
#0,n,n,n,0,0                (t0,n,n,j,k,k),Đ
#0,n,n,n,0,0,0              (t0,n,n,j,k,k,k),Đ
#0,n,n,n,0,0,0,0            (t0,n,n,j,k,k,k,k),Đ
#0,n,n,n,0,0,0,0,5          (t0,n,n,j,k,k,k,k,5),5
#0,n,n,0,0,0,0,n            (t0,n,n,k,k,k,k,j),Ș
#0,n,n,0,0,0,0,n,n          (t0,n,n,k,k,k,k,j,j),Đ
#0,n,n,0,0,0,0,n,n,n        (t0,n,n,k,k,k,k,j,j,j),Đ
#0,n,n,0,0,0,0,n,n,n,5      (t0,n,n,k,k,k,k,j,j,j,5),5
#0,n,n,0,0,n,n,n,0,0        (t0,n,n,k,k,j,j,j,k,k),Ș
#0,0,n,n,n,0,0,n,n,0        (k,k,j,j,j,k,k,n,n,t0),↔
#0,0,n,n,n,0,0,n,0,n        (k,k,j,j,j,k,k,n,t0,n),⇹
#0,0,n,n,n,0,0,n,0,n,5      (k,k,j,j,j,k,k,n,t0,n,5),5
#0,0,n,n,n,n,0,n,0,0        (k,k,j,j,j,n,t0,n,k,k),Ș
#0,0,n,n,n,n,0,n,0,0,6      (k,k,j,j,j,n,t0,n,k,k,6),6
#0,0,n,n,0,0,n,0,n,n        (k,k,j,j,k,k,n,t0,n,j),Ș
#0,0,n,n,0,0,n,0,n,n,8      (k,k,j,j,k,k,n,t0,n,j,8),8
#0,0,n,n,0,n,0,0,n,n        (k,k,j,n,t0,n,k,k,j,j),Ș
#0,0,n,n,0,n,0,0,n,n,3      (k,k,j,n,t0,n,k,k,j,j,3),3
#0,0,n,n,0,n,0,n,n,0        (k,k,j,n,t0,n,k,j,j,k),Ș
#0,0,n,n,0,n,0,n,n,0,6      (k,k,j,n,t0,n,k,j,j,k,6),6
#0,0,n,n,0,n,n,0,n,0        (k,k,j,n,k,j,j,k,n,t0),Ș
#0,0,n,n,0,n,n,0,n,0,4      (k,k,j,n,k,j,j,k,n,t0,4),4
#0,0,n,n,0,n,0,n,0,n        (k,k,j,n,k,j,t0,n,k,j),Ș
#0,0,n,n,0,n,0,n,n,0        (k,k,j,n,k,j,t0,n,j,k),⇹
#0,0,n,n,0,n,0,n,n,0,3      (k,k,j,n,k,j,t0,n,j,k,3),3
#0,0,n,n,0,n,0,0,n,n        (k,k,j,n,k,j,t0,k,j,n),Ș
#n,n,0,0,n,0,n,n,0,0        (n,j,k,t0,j,k,n,j,k,k),↔

##END BUILDING STACK NEEDED FOR CALCULATIONS

##BEGIN CALCULATIONS

#n,n,0,0,n,0,n,n,0,1        (n,j,k,t0,j,k,n,j,k,k+1),⁺
#n,n,0,0,n,0,n,n,0,1,3      (n,j,k,t0,j,k,n,j,k,k+1,3),3
#n,n,0,0,n,0,n,n,0,3        (n,j,k,t0,j,k,n,j,k,3k+3),*
#n,n,0,0,n,0,n,n,0,-3       (n,j,k,t0,j,k,n,j,k,-3k-3),~
#n,n,0,0,n,0,n,n,0,-3,4     (n,j,k,t0,j,k,n,j,k,-3k-3,4),4
#n,n,0,0,n,0,-3,0,n,n       (n,j,k,t0,j,k,-3k-3,k,j,n),Ș
#n,n,0,0,n,0,-3,0,0         (n,j,k,t0,j,k,-3k-3,k,j-n),-
#n,n,0,0,n,0,-3,0           (n,j,k,t0,j,k,-3k-3,k+j-n),+
#n,n,0,0,n,0,-3,0           (n,j,k,t0,j,k,-3k-3,q),~ ##q=n-j-k
#n,n,0,0,n,0,-3,0,0         (n,j,k,t0,j,k,-3k-3,q,q),Đ
#n,n,0,0,n,0,-3,0,0,0       (n,j,k,t0,j,k,-3k-3,q,q,q),Đ
#n,n,0,0,n,0,-3,0,0,0,1     (n,j,k,t0,j,k,-3k-3,q,q,q),1
#n,n,0,0,n,0,-3,0,0,0,-1    (n,j,k,t0,j,k,-3k-3,q,q,q,-1),~
#n,n,0,0,n,0,-3,0,0,-1,0    (n,j,k,t0,j,k,-3k-3,q,q,-1,q),⇹
#n,n,0,0,n,0,-3,0,0,1       (n,j,k,t0,j,k,-3k-3,q,q,(-1)^q),^
#n,n,0,0,n,0,-3,0,0,1,4     (n,j,k,t0,j,k,-3k-3,q,q,(-1)^q),4
#n,n,0,0,n,0,1,0,0,-3       (n,j,k,t0,j,k,(-1)^q,q,q,-3k-3),Ș
#n,n,0,0,n,0,1,0,0,3        (n,j,k,t0,j,k,(-1)^q,q,q,3k+3),Å
#n,n,0,0,n,0,1,0,0,3,3      (n,j,k,t0,j,k,(-1)^q,q,q,3k+3,3k+3),Đ
#n,n,0,0,n,0,1,0,0,3,3,3    (n,j,k,t0,j,k,(-1)^q,q,q,3k+3,3k+3,3),3
#n,n,0,0,n,0,1,0,3,3,0      (n,j,k,t0,j,k,(-1)^q,q,3k+3,3k+3,q)Ș
#n,n,0,0,n,0,1,0,3,3        (n,j,k,t0,j,k,(-1)^q,q,3k+3,3k+3+q)+
#n,n,0,0,n,0,1,0,[3]        (n,j,k,t0,j,k,(-1)^q,q,[3k+3...3k+3+q]),Ř

##u=(3k+3)*(3k+4)*...*(3k+3+q)

#n,n,0,0,n,0,1,0,u          (n,j,k,t0,j,k,(-1)^q,q,u),Π
#n,n,0,0,n,0,1,u,0          (n,j,k,t0,j,k,(-1)^q,u,q),⇹
#0,u,1,0,n,0,0,n,n          (q,u,(-1)^q,k,j,t0,k,j,n),↔
#0,u,1,0,n,0,0,n,n,n        (q,u,(-1)^q,k,j,t0,k,j,n,n),Đ
#n,n,n,0,0,n,0,1,u,0        (n,n,j,k,t0,j,k,(-1)^q,u,q),↔
#n,n,n,0,0,n,0,1,u,0,9      (n,n,j,k,t0,j,k,(-1)^q,u,q,9),9
#n,0,u,1,0,n,0,0,n,n        (n,q,u,(-1)^q,k,j,t0,k,j,n),Ș
#n,n,0,0,n,0,1,u,0,n        (n,j,k,t0,j,k,(-1)^q,u,q,n),↔
#n,n,0,0,n,0,1,u,0,n!       (n,j,k,t0,j,k,(-1)^q,u,q,n!),!
#n,n,0,0,n,0,1,u,0,n!,3     (n,j,k,t0,j,k,(-1)^q,u,q,n!,3),3
#n,n,0,0,n,0,1,n!,0,u       (n,j,k,t0,j,k,(-1)^q,n!,q,u),Ș
#n,n,0,0,n,0,1,n!,u,0       (n,j,k,t0,j,k,(-1)^q,n!,u,q),⇹
#n,n,0,0,n,0,1,n!,u,0,3     (n,j,k,t0,j,k,(-1)^q,n!,u,q,3),3
#n,n,0,0,n,0,1,0,u,n!       (n,j,k,t0,j,k,(-1)^q,q,u,n!),Ș
#n,n,0,0,n,0,1,0,u*n!       (n,j,k,t0,j,k,(-1)^q,q,u*n!),*
#n,n,0,0,n,0,1,u*n!,0       (n,j,k,t0,j,k,(-1)^q,u*n!,q),⇹
#n,n,0,0,n,0,1,u,1          (n,j,k,t0,j,k,(-1)^q,u,q!),!
#n,n,0,0,n,0,1,u            (n,j,k,t0,j,k,(-1)^q,u/q!),÷
#n,n,0,0,n,0,u              (n,j,k,t0,j,k,(-1)^q*u/q!),*

##v=(-1)^q*u/q!

#n,n,0,0,n,0,u,3            (n,j,k,t0,j,k,v,3),3
#n,n,0,0,u,0,n              (n,j,k,t0,v,k,j),Ș
#n,n,0,0,u,0,n,n            (n,j,k,t0,v,k,j,j),Đ
#n,n,0,0,u,0,n,n,2          (n,j,k,t0,v,k,j,j,2),2
#n,n,0,0,u,0,n,2,n          (n,j,k,t0,v,k,j,2,j),⇹
#n,n,0,0,u,0,n,2^n          (n,j,k,t0,v,k,j,2^j),^
#n,n,0,0,u,0,2^n,n          (n,j,k,t0,v,k,2^j,j),⇹
#n,n,0,0,u,0,2^n,n!         (n,j,k,t0,v,k,2^j,j!),!
#n,n,0,0,u,0,2^n,n!,3       (n,j,k,t0,v,k,2^j,j!,3),3
#n,n,0,0,u,n!,2^n,0         (n,j,k,t0,v,j!,2^j,k),Ș
#n,n,0,0,u,n!,2^n,0,4       (n,j,k,t0,v,j!,2^j,k,4),4
#n,n,0,0,0,2^n,n!,u         (n,j,k,t0,k,2^j,j!,v),Ș
#n,n,0,0,0,2^n,u,n!         (n,j,k,t0,k,2^j,v,j!),⇹
#n,n,0,0,0,2^n,u/n!         (n,j,k,t0,k,2^j,v/j!),/
#n,n,0,0,0,2^n*u/n!         (n,j,k,t0,k,2^j*v/j!),*

##w=2^j/j!

#n,n,0,0,u,w,0              (n,j,k,t0,v,w,k),⇹
#n,n,0,0,u,w,1              (n,j,k,t0,v,w,k!),!
#n,n,0,0,u,w                (n,j,k,t0,v,w*k!),*
#n,n,0,uw                   (n,j,k,t0+vw*k!),+

## tt=t0+vw*k!

#n,n,uw,0                   (n,j,tt,k),⇹
#n,n,uw,0,0                 (n,j,tt,k,k),Đ
#n,n,uw,0,0,3               (n,j,tt,k,k,3),3
#n,n,0,0,uw                 (n,j,k,k,tt),Ș
#n,n,0,uw,0                 (n,j,k,tt,k),⇹
#n,n,0,uw,-1                (n,j,k,tt,k-1),⁻
#n,n,0,uw,-1,3              (n,j,k,tt,k-1,3),3
#n,n,-1,uw,0                (n,j,k-1,tt,k),Ș

##END CALCULATIONS

#n,n,-1,uw,0                (n,j,k-1,tt,k),ł

##END INNER LOOP

##ENTER OUTER LOOP

#n,n,-1,uw                  (n,j,k-1,tt),ŕ
#n,n,uw,-1                  (n,j,tt,k-1),⇹
#n,n,uw                     (n,j,tt),ŕ
#uw,n,n                     (tt,j,n),⇹
#uw,n,n,n                   (tt,j,n,n),Đ
#n,n,n,uw                   (n,n,j,tt),↔
#n,n,uw,n                   (n,n,tt,j),⇹
#n,n,uw,n,3                 (n,n,tt,j,3),3
#n,n,uw,n                   (n,j,tt,n),Ș
#n,n,n,uw                   (n,j,n,tt),⇹
#n,n,n,uw,3                 (n,j,n,tt,3),3
#n,uw,n,n                   (n,tt,n,j),Ș
#n,uw,n,n,n                 (n,tt,n,j,j),Đ
#n,uw,n,n,n,3               (n,tt,n,j,j,3),3
#n,uw,n,n,n                 (n,tt,j,j,n),Ș
#n,uw,n,n,n                 (n,tt,j,n,j),⇹
#n,uw,n,n,n-1               (n,tt,j,n,j-1),⁻
#n,uw,n,n,n-1,n-1           (n,tt,j,n,j-1,j-1),Đ
#n,uw,n,n,n-1,n-1,5         (n,tt,j,n,j-1,j-1,5),5
#n,n-1,n-1,n,n,uw           (n,j-1,j-1,n,j,tt),Ș
#n,n-1,n-1,n,n,uw,4         (n,j-1,j-1,n,j,tt,4),4
#n,n-1,uw,n,n,n-1           (n,j-1,tt,j,n,j-1),Ș
#n,n-1,uw,n,1               (n,j-1,tt,j,n-j+1),-
#n,n-1,uw,n,1,3             (n,j-1,tt,j,n-j+1,3),3
#n,n-1,1,n,uw               (n,j-1,n-j+1,j,tt),Ș
#n,n-1,1,uw,n               (n,j-1,n-j+1,tt,j),⇹

##RE-ENTER INNER LOOP

#.
#.
#.

##EXIT INNER LOOP


#.
#.
#.


##RE-ENTER INNER LOOP

#.
#.
#.

##EXIT INNER LOOP

##ENTER OUTER LOOP

#.
#.
#.

#n,-1,n+1,tf,0              (n,j-1,n-j+1,tf,j),ł

##EXIT OUTER LOOP

#n,-1,n+1,tf                (n,j-1,n-j+1,tf),ŕ
#n,-1,n+1,tf,3              (n,j-1,n-j+1,tf,3),3
#n,tf,n+1,-1                (n,tf,n-j+1,j-1),Ș
#-1,n+1,tf,n                (j-1,n-j+1,tf,n),↔
#-1,n+1,tf                  (j-1,n-j+1,tf),ŕ
#-1,n+1                     (n,j-1,n-j+1),ƥ   [PRINTS a(n)]
#                           (),ĉ

#
#
#
#
#
#
#
#
#
#
#
#






















#n                                      (n),←
#n,n                                    (n,n),Đ
#n,n!                                   (n,n!),!
#n!,n                                   (n!,n),⇹
#n!,[1,...,n]                           (n!,[1,...,n]),ř
#n!,perm(1...n)                         (n!,perm(1...n)),ᒆ
#perm(1...n),n!                         (perm(1...n),n!),↔
#perm(1...n),n!,0                       (perm(1...n),n!,0),0
#perm(1...n),0,n!                       (perm(1...n),0,n!),⇹

##ENTER LOOP

#perm(1...n),0,n!                       (perm(1...n),0,n!),`
#perm(1...n),0,n!,3                     (perm(1...n),0,n!,3),3
#perm(1...n),n!,0,[12...n]              (perm(1...n),n!,0,[12...n]),Ș
#perm(1...n),n!,0,[11...1]              (perm(1...n),n!,0,[11...1]),₋
#perm(1...n),n!,0,[11...1]              (perm(1...n),n!,0,[11...1]),Å
#perm(1...n),n!,0,[11...1],1            (perm(1...n),n!,0,[11...1],1),1
#perm(1...n),n!,0,1,[11...1]            (perm(1...n),n!,0,1,[11...1]),⇹
#perm(1...n),n!,0,n                     (perm(1...n),n!,0,ɔ1),ɔ
#perm(1...n),n!,0,n,1                   (perm(1...n),n!,0,ɔ1,1),1
#perm(1...n),n!,0,False                 (perm(1...n),n!,0,==1),=
#perm(1...n),n!,0                       (perm(1...n),n!,0+==1),+
#perm(1...n),0,n!                       (perm(1...n),0+==1,n!),⇹
#perm(1...n),0,n!-1                     (perm(1...n),0+==1,n!-1),⁻
#perm(1...n),0,n!-1                     (perm(1...n),0+==1,n!-1),ł

##REPEAT LOOP

#.
#.
#.

#SC,0                                   (SC,0),ł

#EXIT LOOP

#SC                                     (SC),ŕ

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#




