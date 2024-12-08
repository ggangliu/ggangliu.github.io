# Graphviz Dot

Example:

``` dot
digraph "pico-fhgw-topo" {
    bgcolor="lightblue"
    rankdir = TD;
    splines = ortho;
    graph [fontname="Verdana", fontsize="12"];
    node [fontname="Verdana", fontsize="12"];
    edge [fontname="Sans", fontsize="9"];
    
    rms [label="RMS", shape="box", fillcolor=lightyellow, style=filled];
    
    subgraph cluster_fhgw {
        fdd_du [label="FDD DU", shape="box", href="https://www.sphinx-doc.org/", target="_blank"];
        tdd_du [label="TDD DU", shape="box", href="https://www.sphinx-doc.org/", target="_blank"];
        m_fhgw [label="Main FHGW", shape="rectangle", fontcolor=white, fillcolor="#3333ff", style=filled];
        c_fhgw [label="Cascade FHGW", shape="rectangle", fontcolor=white, fillcolor="#3333ff", style=filled];
        ru     [label="RU", shape="circle"];
        
        fdd_du -> m_fhgw [label=" eCPRI "];
        tdd_du -> m_fhgw [label=" eCPRI "];
        m_fhgw -> c_fhgw [label=" CPRI ", style=dashed, arrowhead=none];
        c_fhgw -> ru [label=" CPRI "];
    }
    
    rms -> m_fhgw [label=" MPlane "];
}
```

[Online Editor](http://magjac.com/graphviz-visual-editor/)


<http://magjac.com/graphviz-visual-editor/>