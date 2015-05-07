<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>CH4_GFED4BA_Emissions</sld:Name>
    <sld:UserStyle>
      <sld:Name>CH4_GFED4BA_Emissions</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="interval">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="Gg"/>
              <sld:ColorMapEntry color="#00610d" opacity="1.0" quantity="5" label="0 - 5"/>
              <sld:ColorMapEntry color="#c5db00" opacity="1.0" quantity="10" label="5 - 10"/>
              <sld:ColorMapEntry color="#ffd900" opacity="1.0" quantity="15" label="10 - 15"/>
              <sld:ColorMapEntry color="#ff8400" opacity="1.0" quantity="20" label="15 - 20"/>
              <sld:ColorMapEntry color="#ff2600" opacity="1.0" quantity="25" label="20 - 25"/>

            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>