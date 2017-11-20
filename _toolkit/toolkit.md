---
permalink: /toolkit/
layout: toolkit-layout
title: Toolkit
summary: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue aliquet tincidunt. Cras in libero rhoncus, semper metus eu, finibus nunc. Nunc feugiat lorem tellus, et sollicitudin eros feugiat vitae.'
---


<section class="category category--discover usa-section" id="discover">
  <div class="usa-grid">
{% for toolkit in site.toolkit %}

<span class="anchor" id="{{ 'Title' | slugify }}"></span>
<article class="method" itemscope itemtype="http://schema.org/Article">
  <div class="method--panel method--panel--front">
    <h1 class="method--title" itemprop="headline"><a href="{{ site.baseurl }}{{ toolkit.url }}">
      {{toolkit.title}}
    </a></h1>

    {% comment %}
    {{ toolkit.excerpt }}
    {% endcomment %}


   </div>
<div>

<div class="method--panel method--panel--back">
    <section class="method--section">
      {% assign second_part = toolkit.content %}

      {% comment %}
      {{ second_part | replace_first: toolkit.excerpt, ""}}
      {% endcomment %}

      
     </section>
  </div>
<time datetime="{{ this_method.last_modified_at | date: '%Y-%m-%d' }}" itemprop="datePublished">  {{ this_method.last_modified_at | date: '%B %d, %Y' }}</time>
</div>
</article>

{% endfor  %}

 </div>
</section>
