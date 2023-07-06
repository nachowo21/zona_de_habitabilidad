# formula profe seba 
# temperatura zona habitable = (radio_estrella/((2*distancia)**0.5))* temperatura_estrella
def zona_habitable(T_E,R_E):
    t_zona_h_min = 20 # ejemplo
    # calcular el radio interno y externo 
    distancia = (r_estrella/2)*(T_estrella/T_zona_h)**2
    return distancia 

# formula wikipedia 
# radio interno = [ris -ai(temperatura efectiva de la estrella -ts )**2 - bi (temperatura efectiva de la estrella - ts)**2]*(luminosidad de la estrella)**0.5
# radio exterior = [ros -ao (temperatura efectiva de la estrella -ts)**2 - bo(temperatura efectiva de la estrella -ts)**2 ]*(luminosidad de la estrella)**0.5
def zona_habitable_(t_efectiva,luminosidad):
    ts = 5700
    ris = 0.72
    ros = 1.77
    ai = (2.7619)*(10)**-5
    bi = (3.8095)*(10)**-9
    ao = (1.3786)*(10)**-4
    bo = (1.4286)*(10)**-9

    r_interno = (ris -ai*(t_efectiva-ts)**2 - bi * ((t_efectiva-ts)**2)*(luminosidad)**0.5 )
    r_externo =  (ros -ao*(t_efectiva-ts)**2 - bo * ((t_efectiva-ts)**2)*(luminosidad)**0.5 )

    return(r_interno,r_externo)

