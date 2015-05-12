<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>GriddedLivestock_heads</sld:Name>
    <sld:UserStyle>
      <sld:Name>GriddedLivestock_heads</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="Heads"/>
              <sld:ColorMapEntry color="#92c800" opacity="1.0" quantity="50" label="&gt; 0 - 50"/>
              <sld:ColorMapEntry color="#ffff00" opacity="1.0" quantity="100" label="50 - 100"/>
              <sld:ColorMapEntry color="#ff8400" opacity="1.0" quantity="150" label="100 - 150"/>
              <sld:ColorMapEntry color="#ff2600" opacity="1.0" quantity="99999" label="&gt; 150"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>