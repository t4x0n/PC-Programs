<?xml version="1.0" encoding="UTF-8"?>
<!-- ============================================================= -->
<!--  MODULE:    Saxon shell (pipelining) stylesheet               -->
<!--             HTML Preview with NLM/Pubmed citations            -->
<!--  VERSION:   1.0                                               -->
<!--  DATE:      January 2009                                      -->
<!--                                                               -->
<!-- ============================================================= -->

<!-- ============================================================= -->
<!--  SYSTEM:    NCBI Archiving and Interchange Journal Articles   -->
<!--                                                               -->
<!--  PURPOSE:   Pipelines stylesheets to convert                  -->
<!--             Journal Publishing 3.0 XML as follows:            -->
<!--             1. format citations in NLM/Pubmed style           -->
<!--             2. convert to HTML for preview display            -->
<!--                                                               -->
<!--  PROCESSOR DEPENDENCIES:                                      -->
<!--             Saxon, from Saxonica (www.saxonica.com)           -->
<!--             Tested using Saxon 9.1.0.3 (B and SA)             -->
<!--                                                               -->
<!--  COMPONENTS REQUIRED:                                         -->
<!--             main/shell-utility.xsl, plus all the stylesheets  -->
<!--             named in the $processes variable declaration      -->
<!--                                                               -->
<!--  INPUT:     Journal Publishing 3.0 XML with citations         -->
<!--             in NLM/Pubmed format                              -->
<!--                                                               -->
<!--  OUTPUT:    HTML                                              -->
<!--                                                               -->
<!--  CREATED FOR:                                                 -->
<!--             Digital Archive of Journal Articles               -->
<!--             National Center for Biotechnology Information     -->
<!--                (NCBI)                                         -->
<!--             National Library of Medicine (NLM)                -->
<!--                                                               -->
<!--  CREATED BY:                                                  -->
<!--             Wendell Piez, Mulberry Technologies, Inc.         -->
<!--                                                               -->
<!-- ============================================================= -->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:saxon="http://saxon.sf.net/"
  version="2.0"
  extension-element-prefixes="saxon">

  <xsl:output method="html" omit-xml-declaration="yes"
    encoding="utf-8" indent="no"/>

  <!-- <xsl:output method="xml" omit-xml-declaration="no"
    encoding="utf-8" indent="no"/> -->
  
  <xsl:variable name="processes">
    <!-- format citations in NLM/PMC format -->
    <step>jpub3-preview-xslt/citations-prep/jpub3-PMCcit.xsl</step>
    <!-- convert into HTML for display -->
    <step>jpub3-preview-xslt/main/jpub3-html.xsl</step>
  </xsl:variable>

  <xsl:include href="shell-utility.xsl"/>
  

</xsl:stylesheet>
