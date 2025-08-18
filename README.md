# PythonProyectoFinal
Acá se compartirán todos las tareas relacionadas al proyecto final del curso Técnico de Python.
# Primer Entregable 
# Nombre del Data Set
Porcentaje de la población que usa internet (%), por país y año.
# Justificación de la elección 
  Las cifras del dataset que elegimos muestran cómo ha aumentado el acceso a internet a nivel mundial, y por lo anteriror nos dimos a la tarea de estudiar más a fondo para entender el impacto del acceso al enternet en la sociedad. Elegimos este dataset porque ofrece información histórica de distintos países en muchas epocas o años distintos, lo que nos permite observar cómo ha evolucionado la conectividad digital a lo largo del tiempo. Además, el conjunto de datos muestra el porcentaje de personas que usaban internet en el pasado, lo cual es útil para analizar el crecimiento de la tecnología, identificar desigualdades digitales y de acceso entre países o regiones y explorar la relación entre acceso a internet y desarrollo humano.
  Nos parece importante porque, como estudiantes de Python, nos permite practicar y visualizar tendencias reales que tienen un fuerte vínculo con el avance tecnológico global y el acceso al intenet en practicamente cualquier parte del mundo. También planeamos comparar la evolución y el cambio entre distintos continentes y destacar casos de crecimiento acelerado o estancamiento. La idea principal es aplicar los conceptos que estamos aprendiendo en programación Phyton. Además, este análisis puede servir para proyectos futuros, y nuestros portafolios estudiantiles. Como parte del proyecto, nos gustaría investigar si hay años o regiones donde hubo un aumento mayor o menor en el uso de internet y relacionarlo con ciertos factores como los cambios tecnológicos o eventos globales como la pandemia. También queremos explorar la confiabilidad e incertidumbre del dataset y entender las limitaciones de los datos disponibles, su cobertura y cómo han sido recolectadas los datos a lo largo del tiempo.
# Explicar porqué el data set es de nuestro interés 
  Nos interesa analizar el dataset seleccionado porque queremos entender cómo ha evolucionado el acceso a internet en el mundo y en qué medida esa evolución ha sido equitativa entre los diferentes paises del mundo. El internet es una herramienta fundamental para la educación, el empleo y la comunicación, y queremos estudiar su crecimiento a lo largo del tiempo. Queremos estudiar como ha crecido el acceso en distintas regiones, identificar puntos de inflexión del uso del intenert y pensar en posibles impactos positivos y negativos que ha dejado su uso, como avances tecnológicos o los porblemas de cyberseguridad producto del uso del intenert tambien. 
# Mencionar qué aspectos específicos del dataset planeamos explorar
-Tendencias a lo largo del tiempo: si el acceso a internet ha aumentado consistentemente en todo el mundo desde 1990, y si hay regiones que muestran un crecimiento más acelerado que otras.
-Comparación entre regiones o continentes: Vamos a comparar cómo ha sido el avance del acceso a internet entre diferentes partes del mundo.
-Identificación de desigualdades: Nos interesa detectar si hay desigualdades marcadas entre países desarrollados y en vías de desarrollo y paises del primer mundo. 
-Años especificos de crecimiento: Queremos detectar si hay años en los que el porcentaje de población con acceso a intenet creció más que en otros, y si esto se relaciona con otrs eventos especifos de algún año. 

# Plan de Análisis: Uso del Internet a Nivel Global
Los gráficos evidencian de que forma la conectividad digital no está equitativamente distribuida. Mientras que regiones desarrolladas muestran un alto porcentaje de población con acceso a internet, regiones en desarrollo como Africa enfrentan limitaciones significativas, generando dificultades y desigualdades digitales. Esta desigualdad impacta en educación, comercio y participación social, y sugiere que los esfuerzos que si se deberían enfocar en aumentar la infraestructura tecnológica y el acceso económico en las regiones menos conectadas. La distribución por país evidencia que incluso dentro de regiones con buen acceso, aún existen países que necesitan mejorar sus niveles de conectividad para reducir estas diferencias, como aquí en Costa Rica.
# Preguntas de investigación
1.	¿Cómo ha evolucionado el porcentaje de la población con acceso a internet a lo largo del tiempo a nivel global y regional?
2.	¿Existen diferencias significativas en el acceso a internet entre continentes?
3.	¿Existe una correlación entre el porcentaje de la población con acceso a internet y el año?
# Hipótesis iniciales
1.	Se espera observar una tendencia creciente del acceso a internet a nivel global desde el año 1990 hasta la fecha.
2.	Las regiones desarrolladas, como Europa y América del Norte, tendrán mayores porcentajes de acceso a internet que regiones como África o Asia Central.
3.	Se prevé una correlación positiva significativa entre el porcentaje de la población que utiliza internet y variables socioeconómicas (si se integran otras bases de datos complementarias).
# Visualizaciones planeadas
1.	Gráfico de líneas: Se utilizará para mostrar la evolución temporal del acceso a internet, esto permitirá identificar tendencias generales.
2.	Gráfico de barras: Se empleará para comparar el porcentaje de acceso a internet entre años.
3. Gráfico de barras: ilustrar el acceso a intenert por país para analizar las brechas existentes. 
4.	Gráfico de dispersión: Mostrará la relación entre el año y el porcentaje de uso de internet, permitiendo analizar la correlación esperada.
5.	Histograma: Mostrará la distribución de países según su porcentaje de población con acceso a internet en un año determinado. Ayudará a identificar cuántos países están en rangos altos, medios o bajos de acceso.
# Metodología
El análisis será realizado en Python utilizando las librerías pandas y matplotlib para gráficos interactivos. Primero se cargará y explorará el dataset, evaluando su estructura, variables y valores faltantes. Luego se realizará un análisis descriptivo general: cálculo de media, mediana, desviación estándar y percentiles.Luego, se agruparán los datos por región y por año para hacer comparaciones y estudiar tendencias. También se calcularán correlaciones entre variables relevantes. Finalmente, se generarán las cinco visualizaciones requeridas para respaldar las respuestas a las preguntas de investigación. Este análisis permitirá entender mejor cómo se ha distribuido el acceso a internet en el mundo, y cómo se relaciona con el contexto regional y económico.

# Análisis de resultados
Evolución del Uso de Internet (% Población) por Año:
La gráfica evidencia un crecimiento exponencial en el porcentaje de la población que utiliza internet desde mediados de los años 90. Antes de esa década, el uso era prácticamente nulo, pero a partir del año 2000 comienza un aumento constante y acelerado. Entre 1960–1990 se registra un uso inexistente o marginal (0% de la población). Posteriormente en 1990–2000 se da un crecimiento, aunque todavía limitado. Y a partir del año 2000 se da un crecimiento sostenido, alcanzando más del 80% de la población en 2023 aproximadamente. En relación con la desviación estándar, al inicio (1960–1990), la dispersión es muy baja porque el uso era uniforme (0%). A partir del año 2000, la dispersión aumenta significativamente, lo que indica que en algunos países o regiones la adopción fue mucho más rápida que en otras. En la etapa más reciente, la desviación sigue siendo amplia, mostrando que, aunque el promedio mundial es alto, aún existen diferencias marcadas en el acceso según la región o condiciones socioeconómicas.

Análisis de  Correlación Año vs Uso de Internet:
Antes de 1990, casi todos los valores se concentran en 0%, indicando que el internet no estaba disponible para la mayoría de los países. A partir de mediados de los 90, comienza a observarse una dispersión creciente: algunos países adoptan internet rápidamente, mientras que otros lo hacen de forma más lenta. Desde el 2000, se alcanzan valores cercanos al 00% de la población en algunos países, mostrando una fuerte variabilidad en la adopción global.
La línea de regresión lineal en rojo indica una relación positiva entre el paso de los años y el aumento del porcentaje de usuarios de internet. El coeficiente de correlación reportado es r = 0.72, lo que significa una correlación fuerte y positiva. Sin embargo, la nube de dispersión deja ver que la relación no es estrictamente lineal, sino más bien de tipo exponencial. Por lo que se dice que el internet se ha expandido de manera desigual según el país y el año, pero la tendencia general es que cada año, más personas en el mundo se conectan. 


# Conclusiones
El internet pasó de ser una herramienta marginal para convertirse en un servicio casi universal en apenas tres décadas. Aun así, la amplitud de la desviación estándar revela desigualdades significativas en el acceso, lo que resalta la importancia de políticas de inclusión digital para cerrar la brecha tecnológica.
Se concluye además que el tiempo es un factor clave en la adopción tecnológica, aunque la dispersión muestra la existencia de una “brecha digital” entre países con alta y baja penetración de internet.

 Con respecto al gráfico de barras hay una muestra de que el acceso a Internet cmabia bastante según la región. Europa y América presentan los niveles más altos, cercanos al 80% y 75% respectivamente, lo que refleja un mayor desarrollo en infraestructura digital y mayor uso de las tecnologias.Africa es la region que presenta el menor acceso, masomenos de 35%, evidenciando la desigualdad  que existe entre regiones desarrolladas y en desarrollo. Se puede concluir en la necesidad de  mejorar la conectividad en regiones con menor acceso, para garantizar igualdad de oportunidades en educación, comunicación y economía.

 Por ultimo, con respecto al histograma muestra que la mayoría de los países tienen un acceso a internet entre 50% y 90% de la población, con pocos países por debajo del 40%. A pesar de que algunas regiones como África tienen un acceso menor,  la mayoría de los países si logrado alcanzar niveles altos de conectividad. La distribución también habla sobre la existencia de desigualdades internas en los mismos paises,  mientras algunos países alcanzan casi el 90% dotros todavía presentan dificultades para darle conexion a su población.


