<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>Cultivation_OrganicSoils_Area</sld:Name>
    <sld:UserStyle>
      <sld:Name>Cultivation_OrganicSoils_Area</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="ha (Hectares)"/>
              <sld:ColorMapEntry color="#006b00" opacity="1.0" quantity="10" label="0 - 10"/>
              <sld:ColorMapEntry color="#c5db00" opacity="1.0" quantity="25" label="10 - 25"/>
              <sld:ColorMapEntry color="#ffd900" opacity="1.0" quantity="40" label="25 - 40"/>
              <sld:ColorMapEntry color="#ff8400" opacity="1.0" quantity="60" label="40 - 60"/>
              <sld:ColorMapEntry color="#ff2600" opacity="1.0" quantity="90" label="60 - 90"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>