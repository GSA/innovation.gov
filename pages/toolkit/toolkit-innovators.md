---
layout: toolkit-subpage
title: Engage Innovators and Outside Government
description: Lorem ipsum dolor sit amet,
vertical: innovators
permalink: /toolkit/innovators
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit Lorem ipsum dolor sit amet, consectetur adipiscing. 
class: innovators-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}