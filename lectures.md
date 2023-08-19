---
layout: page
title: Material de clases
description: Listing of course modules and topics.
---

# Material de clases

Datasets (para los casos de aplicación):
- Manifesto Project (cased): [descargar](/esanNLP/resources/datasets/manifesto_cased.df) 
- Manifesto Project (uncased): [descargar](/esanNLP/resources/datasets/manifesto_uncased.df) 

Link del repositorio con archivos de utilidades:
- [Github](https://github.com/paoloMaldonado/esanNLP_resources)

{% for module in site.modules %}
{{ module }}
{% endfor %}
