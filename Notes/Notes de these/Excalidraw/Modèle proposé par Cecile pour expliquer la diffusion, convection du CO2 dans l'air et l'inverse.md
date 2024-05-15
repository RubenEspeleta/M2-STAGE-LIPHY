On etablie un bilan de matière sur une section de la colonne:

![[Drawing 2024-03-05 12.03.40.excalidraw.png]]

$$\frac{\partial C_{CO_2}}{\partial t}\Delta z=j_d(z,t)+j_c(z,t)-j_d(z+\Delta z, t)-j_c(z+\Delta z, t)$$
$$\frac{\partial C_{CO_2}}{\partial t} \Delta z=-\frac{\partial j_d}{\partial z} \Delta z-\frac{\partial j_c}{\partial z}\Delta z$$

La loi de Fick: $j_d=-D\frac{\partial C_{CO_2}}{\partial z}e_z$ for diffusion, et $j_c=Cv$ 

On considère $v$ constant pendant les experiences (hypothese):

- Pour 100% $CO_2$ debit:

$$v=\frac{Q}{S}=\frac{1000 ml/min}{12.5 \times 9 cm^2}=\frac{1.667 \times 10^{-5} m^3/s }{0.01125 m^2}=1.48 \times 10^{-3} m/s $$

On remplace la loi de Fick dans l'equation du bilan de matière et on obtient:

$$\frac{\partial C_{CO_2}}{\partial t}=D\frac{\partial^2C_{CO_2}}{\partial z^2}-v\frac{\partial C_{CO_2}}{\partial z} $$
On regarde separement le cas où la diffusion gagne et quand la convenction gagne. 
Pour en savoir, on regarde le nombre de Peclet:

$$P_c=\frac{L_cv}{D}$$
$$ L_c \approx \sqrt{Dt}$$
$$P_c=v\sqrt{\frac{t}{D}}$$
Pour le cas quand $P_c=1$, $t=\frac{D}{v^2}$ :
$$t=\frac{D}{v^2}= \frac{1.6 \times 10^{-5}m^2/s}{(1.48 \times 10^{-3}m/s)^2}=7.304 s$$

Quand $t<7.304$ s, c'est la diffusion qui domine. Après 7.304 s, c'est la convection. 
Si on reprend la colonne, au bout de 7.304 s, à quelle hauteur est le font de concentrat?
$$L_d=\sqrt{Dt}$$
$$L_d=0.01 m $$

Àpres 1 cm, c'est l'advection. Le capteur est à 60 cm en haut de la colonne donc on commence a sentir le $CO_2$ sur le capteur quand par convection le $CO_2$ est monté 60 cm - 1 cm = 59 cm. 

Pour monter 59 cm par convection on a besion de:
$$t_A=\frac{L_c}{v}=\frac{0,59 m}{1.48 \times 10^{-3}m/s}=398.648s$$
Pour que le capteur sente le $CO_2$ on a besoin d'attendre $t+t_A$ donc 406s. 

Pour que le capteur de $CO_2$ soit à 100% $CO_2$ il faut parcourir les 1 cm de diffussion en advection, donc:
$$t_{A2}=\frac{0.01m}{1.48 \times 10^{-3} m/s}=6.756 s$$
![[Drawing 2024-03-05 15.23.36.excalidraw.png]]

