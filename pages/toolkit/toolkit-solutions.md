---
layout: toolkit-subpage
title: Solve Governmental and Societal Problems
description: Lorem ipsum dolor sit amet,
vertical: solutions
permalink: /toolkit/solutions/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit Lorem ipsum dolor sit amet, consectetur adipiscing. 
class: solutions-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}

<div class="culture-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#cops">Communities of Practice</a>
	<a class="usa-button" href="#grand-challenges">Grand Challenges</a>
	</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}