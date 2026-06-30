# Proyecto: Juego de Piedra, Papel o Tijera con Puntuación Dinámica

## Integrantes
* Sebastián Maldonado // Carrera de Ingeniería en Sistemas

## Objetivo del Sistema
Desarrollar una aplicación interactiva basada en consola que permita automatizar el juego clásico de "Piedra, Papel o Tijera", aplicando principios fundamentales de lógica algorítmica, toma de decisiones condicionales y control de flujo mediante bucles continuos. El sistema evalúa las jugadas del usuario frente a una simulación aleatoria de la computadora, manteniendo un marcador persistente hasta que el usuario decida finalizar la sesión de manera controlada.

## Descripción de Funcionalidades
* **Validación y Control de Entradas:** El sistema restringe el ingreso del usuario únicamente a opciones válidas (números del 1 al 4), manejando excepciones lógicas para evitar que el programa colapse ante datos incorrectos.
* **Simulación de Inteligencia Artificial (Azar):** Implementación de un algoritmo de aleatoriedad que simula de forma equitativa las decisiones de la máquina en cada ronda.
* **Procesamiento de Reglas del Juego:** Evaluación mediante estructuras condicionales anidadas y lógica booleana para comparar las jugadas y dictaminar de forma inmediata si existe un empate, una victoria o una derrota.
* **Sistema de Puntuación Persistente:** Contadores acumulativos integrados que actualizan los marcadores globales del jugador y de la computadora en tiempo real tras cada interacción.
* **Cierre de Sesión Estructurado:** Inclusión de una opción de salida (Opción 4) encargada de romper el bucle principal de manera segura, despidiendo al usuario y mostrando los resultados finales.

## Diagramas del Sistema
* **Diagrama de Funcionalidad:** El archivo `JUEGO_PIEDRA_PAPEL_TIJERA.png` (desarrollado inicialmente en Raptor) detalla el flujo lógico secuencial, las condiciones y los ciclos iterativos del programa.
* **Diagrama de Arquitectura:** El sistema sigue una arquitectura monolítica simple basada en capas: 
  `Entrada (Consola de Usuario) ➔ Procesamiento (Lógica de Python con Librería Random) ➔ Salida (Consola de Resultados y Marcador)`.

## Fecha
Junio 2026
