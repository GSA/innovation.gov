---
layout: toolkit-subpage
title: Improve Government Services Delivery
description: Innovative methods to innovate like human-centered design, Lean and Agile, and evidence-based decision-making.
vertical: delivery
permalink: /toolkit/delivery/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit provides approaches, policies, and resources to build a better government through innovation.
class: delivery-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}


<div class="delivery-background toolkit-button-group">
	<div class="usa-grid">
	<a class="usa-button" href="#human-centered">Human-Centered Design</a>
	<a class="usa-button" href="#agile">Agile</a>
	<a class="usa-button" href="#lean">Lean Startup</a>
	<a class="usa-button" href="#decision-making">Evidence-Based Decision Making</a>
	</div>
</div>

{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

{% include box-get-connected.html %}
