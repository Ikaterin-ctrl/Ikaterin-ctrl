<div align="center">

<img src="assets/banner.svg" alt="Catarina Costa — dev que se apaixonou por IA" width="100%"/>

</div>

<br/>

Comecei como **dev**: sites, landing pages, sistemas com banco de dados, um projeto atrás do outro.
No meio do caminho esbarrei em **IA** e me apaixonei. Hoje junto as duas coisas como dev de **IA Generativa** na consultoria de tecnologia da **IBM Brasil**: construo agentes, os pipelines que alimentam as bases de conhecimento deles e, quando algo quebra em produção, abro os traces e sigo o rastro até a causa raiz.

> Meu momento favorito no trabalho é quando algo que **"funciona"** não deveria estar funcionando.
> Uma vez achei um teste que passava só por acaso — e foi aí que entendi que o que eu gosto mesmo é de descobrir **o porquê** das coisas. 🦇

<div align="center">
<img src="assets/status.svg" alt="Ficha de personagem: status e skills" width="100%"/>
</div>

<br/>

<img src="assets/div-origem.svg" alt="Origin story" width="100%"/>

<div align="center">
<img src="assets/worldmap.svg" alt="Minha jornada: web, backend, dados, IA generativa" width="100%"/>
</div>

A base de dev é o que me faz diferente na IA: eu não só escrevo prompts — eu construo o pipeline, o backend e a automação em volta deles.

<img src="assets/div-boss.svg" alt="Boss fights" width="100%"/>

Bugs de LLM em produção não aparecem no stack trace. Alguns que já derrotei:

| 👾 Boss | O que estava acontecendo | Golpe final |
|---|---|---|
| **O Teste Sortudo** | Um teste "passava" só porque um trecho concorrente não chegava ao contexto | 4 traces, 3 cenários, 4 causas raiz sobrepostas — e o falso positivo desmascarado |
| **O Roteador Esquecido** | No 2º turno o roteador repassava só a continuação, sem a pergunta original | Rastreei o que o especialista realmente recebia |
| **A Brevidade Tirana** | A regra "seja breve" vencia a de completude e descartava alertas importantes | 3 iterações de prompt + validação em cada ambiente |
| **A Resposta Escondida** | O conteúdo existia na base, mas só era achado com as palavras exatas do manual | Diagnóstico de *semantic mismatch* comparando dois traces |

<img src="assets/div-inv.svg" alt="Inventário" width="100%"/>

<div align="center">

**⚔️ dev**<br/>
<img src="https://img.shields.io/badge/Python-282a36?style=for-the-badge&logo=python&logoColor=50fa7b"/>
<img src="https://img.shields.io/badge/JavaScript-282a36?style=for-the-badge&logo=javascript&logoColor=f1fa8c"/>
<img src="https://img.shields.io/badge/HTML5-282a36?style=for-the-badge&logo=html5&logoColor=ffb86c"/>
<img src="https://img.shields.io/badge/CSS3-282a36?style=for-the-badge&logo=css&logoColor=bd93f9"/>
<img src="https://img.shields.io/badge/FastAPI-282a36?style=for-the-badge&logo=fastapi&logoColor=8be9fd"/>
<img src="https://img.shields.io/badge/Pydantic_v2-282a36?style=for-the-badge&logo=pydantic&logoColor=ff79c6"/>
<img src="https://img.shields.io/badge/SQL_%2F_PL--SQL-282a36?style=for-the-badge&logo=databricks&logoColor=ff5555"/>
<img src="https://img.shields.io/badge/Firebase-282a36?style=for-the-badge&logo=firebase&logoColor=ffb86c"/>
<img src="https://img.shields.io/badge/Git-282a36?style=for-the-badge&logo=git&logoColor=ff5555"/>
<img src="https://img.shields.io/badge/Postman-282a36?style=for-the-badge&logo=postman&logoColor=ffb86c"/>

**🔮 magia (IA)**<br/>
<img src="https://img.shields.io/badge/Agentes_de_IA-282a36?style=for-the-badge&logo=probot&logoColor=ff79c6"/>
<img src="https://img.shields.io/badge/RAG-282a36?style=for-the-badge&logo=elasticsearch&logoColor=bd93f9"/>
<img src="https://img.shields.io/badge/VLMs_%2F_OCR-282a36?style=for-the-badge&logo=opencv&logoColor=f1fa8c"/>
<img src="https://img.shields.io/badge/Prompt_Engineering-282a36?style=for-the-badge&logo=googlegemini&logoColor=ffb86c"/>
<img src="https://img.shields.io/badge/IBM_watsonx-282a36?style=for-the-badge&logo=ibmcloud&logoColor=8be9fd"/>
<img src="https://img.shields.io/badge/Jupyter-282a36?style=for-the-badge&logo=jupyter&logoColor=ffb86c"/>
<img src="https://img.shields.io/badge/YAML-282a36?style=for-the-badge&logo=yaml&logoColor=ff5555"/>

**💎 itens raros**<br/>
<img src="https://img.shields.io/badge/IBM-AI_Associate_Data_Scientist-bd93f9?style=flat-square&labelColor=282a36"/>
<img src="https://img.shields.io/badge/IBM-Data_Science_Foundations_L1-bd93f9?style=flat-square&labelColor=282a36"/>
<img src="https://img.shields.io/badge/IBM-Data_Science_Methodologies-bd93f9?style=flat-square&labelColor=282a36"/>

</div>

<img src="assets/div-save.svg" alt="Save files" width="100%"/>

<table>
<tr>
<td width="50%" valign="top">

### 🧠 [MindED](https://github.com/Ikaterin-ctrl/MindED)
Sou neurodivergente e passei boa parte da escola tentando aprender num sistema que ensina todo mundo igual. O MindED existe pra que outros estudantes não passem por isso sozinhos: reestrutura textos complexos, quebra conteúdo em microtarefas e gera analogias sob controle.

`Python` `FastAPI` `Pydantic v2` `LLMs`

</td>
<td width="50%" valign="top">

### 🔍 Como eu caço bugs de LLM
```
1. reproduzir em dev e homologação
2. comparar traces (tools, chunks, msgs)
3. diff de system prompts entre ambientes
4. corrigir → retestar → checar regressão
5. triar: é o agente ou é a base?
```

</td>
</tr>
</table>

<img src="assets/div-map.svg" alt="Mapa de contribuições" width="100%"/>

<div align="center">
<img src="https://raw.githubusercontent.com/Ikaterin-ctrl/Ikaterin-ctrl/output/snake.svg" alt="Cobrinha comendo minhas contribuições" width="100%"/>
</div>

<img src="assets/div-pm.svg" alt="Mandar mensagem" width="100%"/>

<div align="center">

Bora conversar sobre **dev**, **agentes em produção**, **qualidade de RAG** ou **IA que deixa o aprendizado mais acessível**.

<a href="https://www.linkedin.com/in/catarina-costa-774950350"><img src="https://img.shields.io/badge/LinkedIn-282a36?style=for-the-badge&logo=gitconnected&logoColor=8be9fd"/></a>
<a href="mailto:catarinacostaandradecom@gmail.com"><img src="https://img.shields.io/badge/E--mail-282a36?style=for-the-badge&logo=gmail&logoColor=ff79c6"/></a>

<br/><br/>
<img src="assets/footer.svg" alt="Game saved" width="70%"/>

</div>
