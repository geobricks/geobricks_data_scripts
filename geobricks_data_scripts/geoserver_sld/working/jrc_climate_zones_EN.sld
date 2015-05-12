<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>JRC_CLIMATE_ZONE</sld:Name>
    <sld:UserStyle>
      <sld:Name>JRC_CLIMATE_ZONE</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="values">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label=""/>
              <sld:ColorMapEntry color="#df0015" opacity="1.0" quantity="1" label="1 - Warm temperate moist"/>
              <sld:ColorMapEntry color="#d4002a" opacity="1.0" quantity="2" label="2 - Warm temperate dry"/>
              <sld:ColorMapEntry color="#bf003f" opacity="1.0" quantity="3" label="3 - Cool temperate moist"/>
              <sld:ColorMapEntry color="#aa0055" opacity="1.0" quantity="4" label="4 - Cool temperate dry"/>
              <sld:ColorMapEntry color="#94006a" opacity="1.0" quantity="5" label="5 - Polar moist"/>
              <sld:ColorMapEntry color="#7f007f" opacity="1.0" quantity="6" label="6 - Polar dry"/>
              <sld:ColorMapEntry color="#6a0094" opacity="1.0" quantity="7" label="7 - Boreal moist"/>
              <sld:ColorMapEntry color="#5500aa" opacity="1.0" quantity="8" label="8 - Boreal dry"/>
              <sld:ColorMapEntry color="#3f00bf" opacity="1.0" quantity="9" label="9 - Tropical montane"/>
              <sld:ColorMapEntry color="#2a00d4" opacity="1.0" quantity="10" label="10 - Tropical wet"/>
              <sld:ColorMapEntry color="#1500e9" opacity="1.0" quantity="11" label="11 - Tropical moist"/>
              <sld:ColorMapEntry color="#0c00ff" opacity="1.0" quantity="12" label="12 - Tropical dry"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>