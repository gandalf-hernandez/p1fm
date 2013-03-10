# -*- coding: utf-8 -*-
response = '<?xml version="1.0" encoding="UTF-8"?><Response>%s</Response>'

en = {
        'say': '<Say>%s</Say>',
        'option': '<Say>Press %s for %s</Say>',
        'track': '<Say>now playing %s</Say>%s',
        'main_menu': response % '<Gather action="/genre_menu" method="GET"><Say voice="woman">Press 1 for English</Say><Say language="es">Oprima 2 para Espanol</Say></Gather>',
        'genre_menu': response % '<Gather action="/radio" method="GET">%s</Gather><Say>We didn\'t receive any input. Goodbye!</Say>',
        'error_try_later': response  % '<Say>Oops. Sorry, please try again later.</Say>',
        'radio': response % '<Gather action="/play" method="GET"><Say>%s radio.</Say>%s</Gather>',
        'rickroll': response % '<Play loop="10">https://dl.dropbox.com/u/11675551/rickroll.mp3</Play>',
}
es = {
        'say': '<Say language="es">%s</Say>',
        'option': '<Say language="es">Oprima %s para %s</Say>',
        'track': '<Say language="es">ahora tocando %s</Say>%s',
        'genre_menu': response % '<Gather action="/radio?language=es" method="GET">%s</Gather><Say language="es">No ha elegido ninguna opción. Adios!</Say>',
        'error_try_later': response  % '<Say language="es">Oops. Perdona, por favor intenta mas tarde later.</Say>',
        'radio': response % '<Gather action="/radio?language=es" method="GET"><Say language="es">Radio %s.</Say>%s</Gather>',
}

#backfill
for key in en:
    es.setdefault(key, en[key])
