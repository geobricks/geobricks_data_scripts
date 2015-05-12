<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>NonTropical_Forests_FuelBiomass</sld:Name>
    <sld:UserStyle>
      <sld:Name>NonTropical_Forests_FuelBiomass</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001" label="T (Dry Matter)/Ha"/>
              <sld:ColorMapEntry color="#bed2ff" opacity="1.0" quantity="41.1" label="All boreal forests: 41"/>
              <sld:ColorMapEntry color="#d3ffbe" opacity="1.0" quantity="50.5" label="All &quot;other&quot; temperate forests: 50.4"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>