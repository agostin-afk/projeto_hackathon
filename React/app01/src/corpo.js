import React from 'react'

export default function Corpo(props){
    return(
        <section class='Corpo'>
            <h1 id='corpoh1'>Esse é o corpo </h1>
            <p>Seu nome é: {props.nome}</p>
            <p>Você possui {props.peso}kg</p>
            <p>E tem {props.idade} anos</p>
        </section>
    )
}