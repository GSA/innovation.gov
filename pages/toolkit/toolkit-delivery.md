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


{% include toolkit-verticals.html %}

<a class="usa-button" href="#agile">{{ page.skip-link }}</a>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}