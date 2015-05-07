<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>CO2_GFED4BA_Emissions</sld:Name>
    <sld:UserStyle>
      <sld:Name>CO2_GFED4BA_Emissions</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="Gg"/>
              <sld:ColorMapEntry color="#619900" opacity="1.0" quantity="400" label="0 - 400"/>
              <sld:ColorMapEntry color="#c5db00" opacity="1.0" quantity="800" label="400 - 800"/>
              <sld:ColorMapEntry color="#ffd900" opacity="1.0" quantity="1200" label="800 - 1,200"/>
              <sld:ColorMapEntry color="#ff8400" opacity="1.0" quantity="1600" label="1,200 - 1,600"/>
              <sld:ColorMapEntry color="#ff2600" opacity="1.0" quantity="2000" label="1,600 - 1,200"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>