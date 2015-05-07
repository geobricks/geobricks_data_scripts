<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>Cultivation_OrganicSoils_N2O_emissions</sld:Name>
    <sld:UserStyle>
      <sld:Name>Cultivation_OrganicSoils_N2O_emissions</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="Gg"/>
              <sld:ColorMapEntry color="#00610c" opacity="1.0" quantity="0.1" label="0 - 0.10"/>
              <sld:ColorMapEntry color="#8bb500" opacity="1.0" quantity="0.15" label="0.10 - 0.15"/>
              <sld:ColorMapEntry color="#d7e600" opacity="1.0" quantity="0.2" label="0.15 - 0.20"/>
              <sld:ColorMapEntry color="#ffe600" opacity="1.0" quantity="0.25" label="0.20 - 0.25"/>
              <sld:ColorMapEntry color="#ffa600" opacity="1.0" quantity="0.3" label="0.25 - 0.30"/>
              <sld:ColorMapEntry color="#ff6e00" opacity="1.0" quantity="0.35" label="0.30 - 0.35"/>
              <sld:ColorMapEntry color="#ff2200" opacity="1.0" quantity="0.4" label="0.35 - 0.40"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>