import React from 'react';

export default function Relogio(){
    return(
        <p id='relogio'>São : {new Date().toLocaleTimeString()} horas</p>
    )
}
