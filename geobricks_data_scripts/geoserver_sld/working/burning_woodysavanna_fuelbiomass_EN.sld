<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>WoodySavanna_FuelBiomass</sld:Name>
    <sld:UserStyle>
      <sld:Name>WoodySavanna_FuelBiomass</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="T (Dry Matter)/Ha"/>
              <sld:ColorMapEntry color="#ffd37f" opacity="1.0" quantity="3.31" label="Savanna Woodland: 3.3"/>
              <sld:ColorMapEntry color="#a87000" opacity="1.0" quantity="6.1" label="Tropical Savanna: 6"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>