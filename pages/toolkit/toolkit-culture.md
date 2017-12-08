---
layout: toolkit-subpage
title: Build a 21st Century Culture and Workforce
description: Improved hiring practices and procurement and acquisitions to create a culture of and overcome barriers to innovation.
vertical: culture
permalink: /toolkit/culture/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit provides approaches, policies, and resources to build a better government through innovation.
class: culture-background
---

{% include toolkit-banner.html %}

{% include toolkit-verticals.html %}

<div class="culture-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#innovation-culture">Creating a Culture of Innovation</a>
	<a class="usa-button" href="#innovation-lab">Launching an Innovation Lab</a>
	<a class="usa-button" href="#CINO">Hiring a Chief Innovation Officer</a>
	<a class="usa-button" href="#tour-of-duty">Tour of Duty Hiring</a>
	<a class="usa-button" href="#acquisitions">Innovative Acquisitions and Procurement</a>
	</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

{% include box-get-connected.html %}
