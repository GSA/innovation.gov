---
layout: toolkit-subpage
title: Build a 21st Century Culture and Workforce
description:
vertical: culture
permalink: /toolkit/culture/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit provides approaches and resources to build a better government through innovation.
class: culture-background
---

{% include toolkit-banner.html %}

{% include toolkit-verticals.html %}

<div class="culture-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#innovation-culture">Culture of Innovation</a>
	<a class="usa-button" href="#innovation-lab">Innovation Labs</a>
	<a class="usa-button" href="#CINO">Chief Innovation Officer</a>
	<a class="usa-button" href="#tour-of-duty">Tour of Duty Hiring</a>
	<a class="usa-button" href="#acquisitions">Acquisitions and Procurement</a>
	</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

<div class="usa-grid usa-footer-return-to-top">
	<a href="#">Return to top</a>
</div>

{% include box-get-connected.html %}
