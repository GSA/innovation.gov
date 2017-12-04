---
layout: toolkit-subpage
title: Build a 21st Century Culture and Workforce
description: Lorem ipsum dolor sit amet,
vertical: culture
permalink: /toolkit/culture/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit Lorem ipsum dolor sit amet, consectetur adipiscing. 
class: culture-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}

<div class="culture-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#acquisitions">Innovative Acquisitions and Procurement</a>
	<a class="usa-button" href="#CINO">Hiring a Chief Innovation Officer</a>
	<a class="usa-button" href="#innovation-culture">Creating a Culture of Innovation</a>
	<a class="usa-button" href="#innovation-lab">Launching an Innovation Lab</a>
	<a class="usa-button" href="#tour-of-duty">Tour of Duty Hiring</a>
	</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

{% include box-get-connected.html %}