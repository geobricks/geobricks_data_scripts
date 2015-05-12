<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>GFED4_BurnedArea</sld:Name>
    <sld:UserStyle>
      <sld:Name>GFED4_BurnedArea</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="ha (Hectares)"/>
              <sld:ColorMapEntry color="#ffffb2" opacity="1.0" quantity="100" label="Low (0 - 100)"/>
              <sld:ColorMapEntry color="#fecc5c" opacity="1.0" quantity="1000" label="Low - Average (100 - 1,000)"/>
              <sld:ColorMapEntry color="#fd8d3c" opacity="1.0" quantity="5000" label="Average (1,000 - 5,000)"/>
              <sld:ColorMapEntry color="#f03b20" opacity="1.0" quantity="10000" label="High - Average (5,000 - 10,000)"/>
              <sld:ColorMapEntry color="#bd0026" opacity="1.0" quantity="100000" label="High (&gt; 10,000)"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>