<?xml version="1.0" encoding="UTF-8"?><sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>GLC2000</sld:Name>
    <sld:UserStyle>
      <sld:Name>GLC2000</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Geometry>
              <ogc:PropertyName>grid</ogc:PropertyName>
            </sld:Geometry>
            <sld:ColorMap type="values">
              <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001"  label="GLC2000 Land Cover"/>
              <sld:ColorMapEntry color="#ffea9e" opacity="1.0" quantity="13" label="Herbaceous Cover, closed-open"/>
              <sld:ColorMapEntry color="#decaa1" opacity="1.0" quantity="14" label="Sparse herbaceous or sparse shrub cover"/>
              <sld:ColorMapEntry color="#009696" opacity="1.0" quantity="15" label="Regularly flooded shrub and/or herbaceous cover"/>
              <sld:ColorMapEntry color="#ffe0e5" opacity="1.0" quantity="16" label="Cultivated and managed areas"/>
              <sld:ColorMapEntry color="#ff75e8" opacity="1.0" quantity="17" label="Mosaic: Cropland / Tree Cover / Other natural vegetation"/>
              <sld:ColorMapEntry color="#ca8aff" opacity="1.0" quantity="18" label="Mosaic: Cropland / Shrub and/or grass cover"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>