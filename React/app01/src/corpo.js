import React from 'react'
import Relogio from  './Relogio'
export default function Corpo(props){
    return(
        <section className='Corpo'>
            <h1 id='corpoh1'>Esse é o corpo </h1>
            <p>Seu nome é: {props.nome}</p>
            <p>Você possui {props.peso}kg</p>
            <p>E tem {props.idade} anos</p>
            <p>Horario atual: <Relogio/></p>
            
        </section>
    )
}