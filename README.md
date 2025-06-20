# 🐍 Ejercicios de Condicionales en Python

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

*Material educativo para la materia Programación 1 - Tecnicatura Universitaria en Programación*

</div>

## 📋 Descripción

Este repositorio contiene una colección de **20 ejercicios progresivos** diseñados para enseñar y practicar estructuras condicionales en Python. Los ejercicios fueron específicamente creados para estudiantes de la Tecnicatura Universitaria en Programación de la Universidad Tecnológica Nacional **(UTN)**.

### 🎯 Objetivos de Aprendizaje

- ✅ Dominar las estructuras condicionales (`if`, `elif`, `else`)
- ✅ Aplicar operadores de comparación y lógicos
- ✅ Desarrollar lógica de programación
- ✅ Practicar validación de entrada de datos
- ✅ Implementar soluciones a problemas reales

## 📁 Estructura del Proyecto

```
Ejercicios-Python-Condicionales/
│
├── README.md
└── Python - Condicionales/
    ├── Ejercicio 1/
    │   ├── Consigna Ejercicio 1.py
    │   └── Solución Ejercicio 1.py
    ├── Ejercicio 2/
    │   ├── Consigna Ejercicio 2.py
    │   └── Solución Ejercicio 2.py
    ├── Ejercicio 3/
    │   ├── Consigna Ejercicio 3.py
    │   └── Solución Ejercicio 3.py
    ├── ...
    └── Ejercicio 20/
        ├── Consigna Ejercicio 20.py
        └── Solución Ejercicio 20.py
```

## 🚀 Cómo Usar Este Repositorio

### Para Estudiantes:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/ejercicios-condicionales-python.git
   cd ejercicios-condicionales-python
   ```

2. **Resuelve los ejercicios en orden:**
   - Lee la consigna de cada ejercicio
   - Intenta resolverlo por tu cuenta
   - Compara tu solución con la proporcionada
   - Ejecuta el código para verificar que funciona

3. **Ejecuta un ejercicio:**
   ```bash
   python ejercicios/ejercicio_01.py
   ```
También puedes utilizar tu editor de código favorito. Por ejemplo: Visual Studio Code.

### Para Profesores:

- Utiliza los ejercicios como material de clase
- Asigna ejercicios específicos según el nivel del grupo
- Modifica las consignas según tus necesidades
- Usa las soluciones como guía de corrección

## 📚 Lista de Ejercicios

| # | Ejercicio | Dificultad | Conceptos Clave |
|---|-----------|------------|-----------------|
| 01 | Número Positivo/Negativo | 🟢 Básico | `if`, `elif`, `else` |
| 02 | Mayor de Edad | 🟢 Básico | Operadores de comparación |
| 03 | Par o Impar | 🟢 Básico | Operador módulo `%` |
| 04 | Mayor de Dos Números | 🟢 Básico | Comparación múltiple |
| 05 | Sistema de Calificaciones | 🟡 Intermedio | Rangos numéricos |
| 06 | Días de la Semana | 🟡 Intermedio | Múltiples condiciones |
| 07 | Año Bisiesto | 🟡 Intermedio | Operadores lógicos |
| 08 | Calculadora Simple | 🟡 Intermedio | Validación de entrada |
| 09 | Validador de Triángulo | 🟡 Intermedio | Lógica matemática |
| 10 | Sistema de Descuentos | 🟡 Intermedio | Rangos y cálculos |
| 11 | Clasificador de IMC | 🟡 Intermedio | Cálculos y rangos |
| 12 | Juego de Adivinanza | 🟡 Intermedio | Números aleatorios |
| 13 | Validador de Contraseña | 🟠 Avanzado | Validación compleja |
| 14 | Sistema de Notas | 🟠 Avanzado | Promedios y estados |
| 15 | Conversor de Temperatura | 🟠 Avanzado | Múltiples conversiones |
| 16 | Clasificador de Edades | 🟠 Avanzado | Rangos detallados |
| 17 | Factura con IVA | 🟠 Avanzado | Cálculos comerciales |
| 18 | Sistema de Préstamos | 🔴 Experto | Lógica empresarial |
| 19 | Piedra, Papel o Tijeras | 🔴 Experto | Lógica de juegos |
| 20 | Reservas de Hotel | 🔴 Experto | Sistema complejo |

## 🛠️ Requisitos

- **Python 3.6+**
- Editor de código (recomendado: VS Code, PyCharm, o similar)
- Terminal/Línea de comandos

## 💡 Consejos para Estudiantes

### 🎯 Estrategia de Resolución:

1. **Lee la consigna cuidadosamente** - Entiende qué se pide antes de programar
2. **Identifica las condiciones** - ¿Qué decisiones debe tomar el programa?
3. **Planifica la estructura** - Dibuja un diagrama de flujo si es necesario
4. **Codifica paso a paso** - Implementa una condición a la vez
5. **Prueba con diferentes valores** - Verifica todos los casos posibles

### 🔍 Debugging:

- Usa `print()` para ver valores de variables
- Prueba casos extremos (números negativos, cero, valores grandes)
- Verifica la lógica de tus condiciones
- Lee los mensajes de error cuidadosamente

### 📖 Conceptos Importantes:

```python
# Operadores de comparación
==  # Igual a
!=  # Diferente de
>   # Mayor que
<   # Menor que
>=  # Mayor o igual que
<=  # Menor o igual que

# Operadores lógicos
and  # Ambas condiciones deben ser verdaderas
or   # Al menos una condición debe ser verdadera
not  # Invierte el valor de verdad

# Estructura básica
if condicion:
    # código si es verdadero
elif otra_condicion:
    # código si otra_condicion es verdadera
else:
    # código si ninguna condición anterior es verdadera
```

## 🎨 Ejemplos de Uso

### Ejemplo Básico:
```python
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Ejemplo Intermedio:
```python
nota = float(input("Ingresa tu nota: "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 5:
    print("Aprobado")
else:
    print("Desaprobado")
```

### Ejemplo Avanzado:
```python
edad = int(input("Edad: "))
ingresos = float(input("Ingresos: "))

if edad >= 18 and edad <= 65 and ingresos >= 30000:
    print("Califica para préstamo")
else:
    print("No califica")
```

## 📋 Checklist de Progreso

Marca los ejercicios que hayas completado:

- [ ] Ejercicio 1: Número Positivo/Negativo
- [ ] Ejercicio 2: Mayor de Edad
- [ ] Ejercicio 3: Par o Impar
- [ ] Ejercicio 4: Mayor de Dos Números
- [ ] Ejercicio 5: Sistema de Calificaciones
- [ ] Ejercicio 6: Días de la Semana
- [ ] Ejercicio 7: Año Bisiesto
- [ ] Ejercicio 8: Calculadora Simple
- [ ] Ejercicio 9: Validador de Triángulo
- [ ] Ejercicio 10: Sistema de Descuentos
- [ ] Ejercicio 11: Clasificador de IMC
- [ ] Ejercicio 12: Juego de Adivinanza
- [ ] Ejercicio 13: Validador de Contraseña
- [ ] Ejercicio 14: Sistema de Notas
- [ ] Ejercicio 15: Conversor de Temperatura
- [ ] Ejercicio 16: Clasificador de Edades
- [ ] Ejercicio 17: Factura con IVA
- [ ] Ejercicio 18: Sistema de Préstamos
- [ ] Ejercicio 19: Piedra, Papel o Tijeras
- [ ] Ejercicio 20: Reservas de Hotel

## 🏆 Desafíos Adicionales

Una vez completados todos los ejercicios, intenta estos desafíos:

1. **Modifica** los ejercicios para manejar errores de entrada
2. **Combina** varios ejercicios en un programa más grande
3. **Crea** versiones más complejas de los ejercicios existentes
4. **Implementa** logging para registrar las acciones del usuario

## 📚 Recursos Adicionales

### 📖 Documentación:
- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Tutorial de Python en Español](https://tutorial.python.org.ar/)
- [Python para Principiantes](https://www.python.org/about/gettingstarted/)

## ❓ FAQ (Preguntas Frecuentes)

### ❓ ¿En qué orden debo resolver los ejercicios?
**Respuesta:** Es recomendable seguir el orden numérico, ya que la dificultad aumenta progresivamente.

### ❓ ¿Qué hago si no entiendo un ejercicio?
**Respuesta:** 
1. Lee la consigna varias veces
2. Busca conceptos que no entiendas
3. Revisa ejercicios anteriores similares
4. Tómate tu tiempo para pensarlo varias veces.
5. Experimenta, intenta resolverlo de la forma que creas. No tengas miedo a equivocarte.
5. Consulta tus dudas con compañeros o profesores

### ❓ ¿Hay soluciones alternativas?
**Respuesta:** Sí, en programación hay múltiples formas de resolver un problema. Lo importante es que funcione correctamente.

## 📊 Métricas del Proyecto

- **20** ejercicios progresivos
- **3** niveles de dificultad
- **100%** código funcional y probado
- **0** dependencias externas
- **Compatible** con Python 3.6+

## 👥 Créditos

### 👨‍💻 Autor:
**Rodolfo Velasco**
- Estudiante de Tecnicatura Universitaria en Programación (Universidad Tecnológica Nacional)
- Gestor de Contenido - Prácticas Profesionales

---

<div align="center">

**⭐ Recuerda, los errores son parte del aprendizaje ⭐**

**¡Feliz programación! 🐍✨**

</div>