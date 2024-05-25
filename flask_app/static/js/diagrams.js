Viz.instance().then(viz => {
	document.body.appendChild(viz.renderSVGElement("digraph { a -> b }"))
});