<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>HWSD_histosols_Area</sld:Name>
    <sld:UserStyle>
      <sld:Name>HWSD_histosols_Area</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="ha (Hectares)"/>
              <sld:ColorMapEntry color="#edf8fb" opacity="1.0" quantity="5000" label="Very Low (&gt;0 - 5,000)"/>
              <sld:ColorMapEntry color="#b3cde3" opacity="1.0" quantity="15000" label="Low (5,000 - 15,000)"/>
              <sld:ColorMapEntry color="#8c96c6" opacity="1.0" quantity="30000" label="Average (15,000 - 30,000)"/>
              <sld:ColorMapEntry color="#8856a7" opacity="1.0" quantity="45000" label="High (30,000 - 45,000)"/>
              <sld:ColorMapEntry color="#810f7c" opacity="1.0" quantity="61000" label="Very High (45,000 - 60,000)"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>