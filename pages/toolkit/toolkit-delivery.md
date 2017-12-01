---
layout: toolkit-subpage
title: Improve Government Services Delivery
description: Lorem ipsum dolor sit amet,
vertical: delivery
permalink: /toolkit/delivery
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit Lorem ipsum dolor sit amet, consectetur adipiscing. 
class: delivery-background
---

{% include toolkit-banner.html %}

{% include box-toolkit.html %}

{% include toolkit-verticals.html %}


<div class="delivery-background toolkit-button-group">
<div class="usa-grid">
<a class="usa-button" href="#agile">Agile</a>
<a class="usa-button" href="#decision-making">Evidence-Based Decision Making</a>
<a class="usa-button" href="#human-centered">Human-Centered Design</a>
<a class="usa-button" href="#lean">Lean Startup</a>
</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}